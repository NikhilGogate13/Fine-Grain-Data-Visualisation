#!/bin/bash

for i in {1..1000}
do
	echo "$(($RANDOM%1000)) $(($RANDOM%1000))" >> newfile.txt
done
