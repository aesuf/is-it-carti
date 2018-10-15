#! /bin/bash

COUNT=1
for FILE in WAV/*.wav
	do
		echo ":[I]: STARTED $FILE"
		echo ":[I]: Output/$COUNT.CSV"
		./mfcc --input "$FILE" --output Output/"$COUNT".csv --samplingrate 44100
		COUNT=$((COUNT+1))
		echo ":[I]: COMPLETED $FILE"
done
