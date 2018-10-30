#!/bin/sh
ffmpeg -i $1 -ss 00:00:$3 -t 00:00:$4 -async 1 $2

# ./trim-video.sh 1.mkv out.mkv 04 10
