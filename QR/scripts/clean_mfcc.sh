#! /bin/bash

for FILE in carti_CSV/*.csv
	do
	echo ":[I]: Cleaning $FILE"
	echo ":[I]: Output music.csv"
	python clean_mfcc.py -i "$FILE" -o music.csv -c True
done
