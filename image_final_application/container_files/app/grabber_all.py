# -*- coding: utf-8 -*-


import subprocess
import json
import os.path
import argparse
import sys
from fun import *


# HARDCODED PARAMETERS
directory = "/app/"
which_python = "python"



def update_tracks_file(args):



	# EXTRACT ARGUMENTS
	artists_filename = args.artists_filename
	tracks_filename = args.tracks_filename


	requested_artists = []
	with open(artists_filename) as file:
		for l in file:
			thename = l.strip().lower()
			if len(thename)>0:
				requested_artists.append(thename)

	requested_artists = [Get_Artist_Id(item)[1].strip().lower() for item in requested_artists if len(Get_Artist_Id(item)[1])>0]
	requested_artists = list(set(requested_artists))
	print(requested_artists)

	# PATH FILENAME
	saved_tracks_filename = directory + tracks_filename


	# EXISTE-T-IL?
	if os.path.isfile(saved_tracks_filename):
		file_exist = True
	else:
		file_exist = False


	# DEFINITION DES CLEAN REQUESTS ARTISTS ET TRACKS
	if file_exist:
		print("ca exist")
		with open(saved_tracks_filename) as json_file: 
			tracks = json.load(json_file) 
		saved_artists = list(set([item["artist_str"].strip().lower() for item in tracks]))
		print(saved_artists)    
		cleaned_requested_artists = [artist for artist in requested_artists if artist not in saved_artists]
		print(cleaned_requested_artists)

	else:
		print("ca exist pas")
		tracks = []
		cleaned_requested_artists = requested_artists


	# DEFINITION DES COMMANDES BASH
	commandbashes = [which_python + " " + directory + "grabber.py -a " + requested_artist + " -f " + directory + "trackslist/temp.json" for requested_artist in cleaned_requested_artists]


	# RUN LES BASH ET APPEND LES RESULTS
	for commandbash in commandbashes:
		print(commandbash)
		cp = subprocess.run([commandbash],shell = True, capture_output = True)
		print("")
		#print(cp.stdout)
		#print("")
		with open(directory + "trackslist/temp.json") as json_file: 
			temp_tracks = json.load(json_file)
		if len(temp_tracks[0])>0:
			tracks = tracks+temp_tracks


	# SAVE JSON FILE
	print("Save results in json file")
	with open(saved_tracks_filename, 'w') as outfile:
		#json.dump(tracks, outfile)
		json.dump(tracks, outfile,indent=4, sort_keys=True)


	return None








if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument('-a', '--artists_filename')
	parser.add_argument('-f','--tracks_filename')
	args = parser.parse_args()
	update_tracks_file(args)