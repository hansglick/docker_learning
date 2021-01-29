input_file=$1
counter=0

while read line || [ -n "$line" ]

do
	
counter=$(($counter+1))
echo "$line"
echo $counter.json
echo "Grabb tracks on Spotify API ..."
#python grabber.py -a $line -f trackslist/$counter.json
echo ""

done < $input_file

#echo "Assembling and deduplicating tracks ..."
#python assembler.py -i trackslist -o final.json

#echo "Add Youtube Links ..."
#python grabber_youtube_links.py -f final.json

# AVANT DE LANCER CETTE LIGNE VERIFIER QUE CA FONCTIONNE EN SH
#echo "Downloading tracks as mp3s ..."
#sh dwlsongs.sh trackslist/tracks.json