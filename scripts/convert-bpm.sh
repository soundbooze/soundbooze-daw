#!/bin/sh

midicsv $1 out.csv
QN=`echo "60000/$2" | bc`
TEMPO=`echo "$QN * 1000" | bc`
sed -i -e 's/Tempo, [0-9]*/Tempo, '$TEMPO'/g' out.csv
csvmidi out.csv new.mid
rm -f out.csv
