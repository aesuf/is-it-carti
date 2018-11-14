#! /bin/bash

for FILE in Output/*.csv
	do
	echo ":[I]: Cleaning $FILE"
	echo ":[I]: Output music.csv"
	python clean_mfcc.py -i "$FILE" -o music.csv
done
