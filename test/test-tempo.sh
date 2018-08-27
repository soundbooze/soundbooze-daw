#!/bin/sh

# todo
# auto balancing - eq volume effects
# mic - source comparison
# etc/

while [ 1 ]
do
  jack_capture -d 4 -f wav test.wav > /dev/null 2>&1
  ffmpeg -i test.wav out.wav > /dev/null 2>&1
  aubio tempo out.wav
  rm -f test.wav out.wav > /dev/null 2>&1
done
