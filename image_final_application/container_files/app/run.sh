input_file=$1
counter=0

echo "Grabb tracks on Spotify API ..."

while read line || [ -n "$line" ]

do
	
counter=$(($counter+1))
echo "$line"
echo $counter.json
python grabber.py -a $line -f trackslist/$counter.json
echo ""

done < $input_file

echo "Assembling and deduplicating tracks ..."
python assembler.py -i /app/trackslist -o /app/songs/final.json

echo "Add Youtube Links ..."
python grabber_youtube_links.py -f songs/final.json

# AVANT DE LANCER CETTE LIGNE VERIFIER QUE CA FONCTIONNE EN SH
echo "Downloading tracks as mp3s ..."
bash songs/dwlsongs.sh songs/final.json