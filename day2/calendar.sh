#!/bin/bash

YEAR=$1
echo $YEAR

rm -rf $YEAR
mkdir $YEAR

for MONTH in $(seq -f "%02g" 1 12); do
    MONTH_NAME=$(date -d "$YEAR-$MONTH-01" +%b)
    mkdir $YEAR/$MONTH-$MONTH_NAME
    DAYS_IN_MONTH=$(date -d "$YEAR-$MONTH-01 + 1 month - 1 day" +%d)
    for DAY in $(seq -f "%02g" 1 $DAYS_IN_MONTH); do
        DAY_OF_WEEK=$(date -d "$YEAR-$MONTH-$DAY" +%A)
        echo "$YEAR/$MONTH/$DAY is a $DAY_OF_WEEK" > $YEAR/$MONTH-$MONTH_NAME/$DAY.txt
    done
done