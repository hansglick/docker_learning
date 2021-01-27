# LOAD LIBS
import json
from random import shuffle
import os
import argparse
import sys



def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]


def Load_and_Sort(filename):

    """
    Load Json and return a sorted artist/followers list
    """

    # LOAD DATA
    with open(filename) as json_file:
        artists = json.load(json_file)

    # SORT DATA
    L = []
    for k,v in artists.items():
        name = v["name"]
        followers = int(v["followers"])
        L.append((name,followers))
    L.sort(key = lambda a : -a[1])
   
    return L



def Filter_List(L,threshold):
   
    """
    Prend une liste d'artistes/followers et la filtre selon le threshold
    """
   
    # THRESHOLD TYPE
    if threshold > 1:
        threshold_type = "follo"
    else:
        threshold_type = "rate"

    # FILTER THE LIST
    taille_de_la_list = len(L)
    Filtered_List = []

    if threshold_type == "rate":
        for idartist,(artist,_) in enumerate(L):
            rate = idartist / taille_de_la_list
            if threshold>rate:
                Filtered_List.append(artist.lower())
            else:
                break

    if threshold_type == "follo":
        for artist,followers in L:
            if followers<threshold:
                break
            else:
                Filtered_List.append(artist.lower())

    shuffle(Filtered_List)
   
    return Filtered_List


def Filter_List(L,threshold):
   
    """
    Prend une liste d'artistes/followers et la filtre selon le threshold
    """
   
    # THRESHOLD TYPE
    if threshold > 1:
        threshold_type = "follo"
    else:
        threshold_type = "rate"

    # FILTER THE LIST
    taille_de_la_list = len(L)
    Filtered_List = []

    if threshold_type == "rate":
        for idartist,(artist,_) in enumerate(L):
            rate = idartist / taille_de_la_list
            if threshold>rate:
                Filtered_List.append(artist.lower())
            else:
                break

    if threshold_type == "follo":
        for artist,followers in L:
            if followers<threshold:
                break
            else:
                Filtered_List.append(artist.lower())

    shuffle(Filtered_List)
   
    return Filtered_List


def Write_Files(Filtered_List,ndockers,folder_output):
   
    """
    Take Filtered_List and ndockers argument and write files into relevant folders
    """
   
    # MAGIC PADDER
    magic_padder = len(str(ndockers)) + 1
   
    # FOLDER OUTPUT CREATION
    if not os.path.exists(folder_output):
        os.makedirs(folder_output)
   
    # WRITING FILES
    for iditem,item in enumerate(chunks(Filtered_List,ndockers)):
        set_number = str(iditem)
        set_number = set_number.zfill(magic_padder)
        for artist in item:
            with open(folder_output+"set_"+set_number+".txt", 'a') as the_file:
                the_file.write(artist+"\n")
               
    return None



def BigTask(args):
   
    filename = args.filename
    threshold = args.threshold
    ndockers = args.ndockers
    folder_output = args.folder_output
   
    L = Load_and_Sort(filename)
    Filtered_List = Filter_List(L,threshold)
    Write_Files(Filtered_List,ndockers,folder_output)
   
    return None



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='test arguments')
    parser.add_argument("-f","--filename")
    parser.add_argument("-t","--threshold",type=float)
    parser.add_argument("-n","--ndockers",type=int)
    parser.add_argument("-o","--folder_output")
    args = parser.parse_args()
    BigTask(args)

