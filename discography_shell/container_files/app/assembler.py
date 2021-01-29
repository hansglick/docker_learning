import json
import argparse
import os
from os import listdir
from os.path import isfile, join

# LISTER LES JSON FILES
# INPUT : FOLDER PATH
# OUTPUT : LISTE DE JSON FILES

def json_files_retrieving(FOLDER_JSON_FILES):
    
    onlyfiles = [f for f in listdir(FOLDER_JSON_FILES) if isfile(join(FOLDER_JSON_FILES, f))]
    json_files = [FOLDER_JSON_FILES+"/"+item for item in onlyfiles if os.path.splitext(item)[1]==".json"]
    
    return json_files



# RÉCUPERATION DES TRACKS DANS UNE SEULE LISTE
# INPUT : LISTE DE JSON FILES PATH
# OUTPUT : LISTE DE TRACKS

def tracks_assembling(json_files):
    
    L = []
    for json_filename in json_files:
        with open(json_filename) as json_file: 
            tracks = json.load(json_file)
            if len(tracks[0])>0:
                L = L + tracks
    
    return L



# DEDUPLICATION DES TRACKS (CE QUI EST TJRS POSSIBLE)
# INPUT : LISTE DE TRACKS
# OUTPUT : LISTE DE TRACKS DEDUPLIQUEE

def tracks_deduplication(L):
    
    d = {}
    
    for track in L:
        if track["track"] not in d:
            d[track["track"]] = track
    
    JSON_TRACKS = list(d.values())
    
    return JSON_TRACKS




# ECRITURE DU JSON
# INPUT : VARIABLE PYTHON
# INPUT : FOLDER DE RECEPTION
# OUTPUT : ECRITURE DU JSON

def json_writing(JSON_TRACKS,path_filename):
    
    with open(path_filename, 'w') as outfile:
        json.dump(JSON_TRACKS, outfile,indent=4, sort_keys=True)
    
    return None




# MAIN
def Build_Final_Json_Tracks(args):
    
    FOLDER_JSON_FILES = args.FOLDER_JSON_FILES
    FOLDER_JSON_FINAL = args.FOLDER_JSON_FINAL
    
    json_files = json_files_retrieving(FOLDER_JSON_FILES)
    L = tracks_assembling(json_files)
    JSON_TRACKS = tracks_deduplication(L)
    json_writing(JSON_TRACKS,FOLDER_JSON_FINAL)

    print("Number of tracks saved :",len(JSON_TRACKS))
    
    return None





if __name__ =="__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument('-i', '--FOLDER_JSON_FILES')
	parser.add_argument('-o','--FOLDER_JSON_FINAL')
	args = parser.parse_args()
	Build_Final_Json_Tracks(args)

