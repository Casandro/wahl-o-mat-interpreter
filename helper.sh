#!/bin/bash

FILENAME="$1"

if [ ! -f "$FILENAME" ]
then
	echo File not found
	exit
fi


tmp=data
mkdir -p "$tmp"

ssconvert -v "$FILENAME" -S $tmp/%s.csv

for file in $tmp/*.*.csv
do
	bn=$(basename "$file" .csv)
	echo $bn
	./wahl-o-mat-distanzen.py "$file"
	echo -e "\n\n"
done

rm -r "$tmp"
