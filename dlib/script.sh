#!/bin/bash

for i in {1..10}
do
	echo "$(($RANDOM%100)) $(($RANDOM%100))" >> newfile.txt
done
