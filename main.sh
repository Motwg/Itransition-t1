#!/bin/bash
# I choose bash over another programing languages only to challenge myself
# it may take ca. 30s-1min to process the file
echo "Starting script"
file=$(<"$1")
IFS=$'\n' string_array=( $(sed 's/\"/\"\n/g' <<< "$file"))

for i in "${!string_array[@]}"
do
    # not in quotes -> filter
    if (( $i % 2 == 0 )); then
        string_array[$i]="$(tr ':=>' '\"\":' <<< ${string_array[$i]})"
    fi
done
(IFS=; echo "${string_array[*]}") > out.json
echo "JSON converted"

source ./.venv/bin/activate
python3 -m insert.py
echo "Done"
