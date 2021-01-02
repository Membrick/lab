#!/bin/bash
filename=./backup.sh
bck=/home/d10/Downloads
read me
a_me=$(whoami)
echo "$a_me"

if [[ -d "$me" -eq "$a_me" ]]; then
	(cp "$filename" "$bck")
else
    echo "File does not exist you maniac"
fi
