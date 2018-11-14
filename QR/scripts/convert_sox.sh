#! /bin/bash

COUNT=1
for FILE in Carti_Songs/*.mp3
	do
		echo ":[I]: STARTED $FILE"
		echo ":[I]: Carti_Songs_WAV/$COUNT.wav"
		sox -v 0.99 "$FILE" Carti_Songs_WAV/$COUNT.wav
		COUNT=$((COUNT+1))
		echo ":[I]: FINISHED $FILE"
done
