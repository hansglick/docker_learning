# SELECTION DES TRACKS A TELECHARGER
JSONFILE=$1
#OUTPUTFOLDER=$2

jq '.[0:6]' < $JSONFILE | jq '.[] .youtube[] .id' > someids.txt
filename="someids.txt"


# DWL MP3S
while read line; do

youtubeid="${line%\"}"
youtubeid="${youtubeid#\"}"
myurl="https://www.youtube.com/watch?v=${youtubeid}"
yid="${youtubeid}.mp3"

echo "$youtubeid"
echo "dwl song"
youtube-dl -x --audio-format mp3 -o "songs/%(id)s.%(ext)s" --audio-quality 9 $myurl
#echo "dwl comments"
#python dwl_comments.py --youtubeid  $youtubeid --output "${OUTPUTFOLDER}/${youtubeid}.json"
#echo ""

done < $filename


# REMOVE USELESS TEMP FILES
rm $filename