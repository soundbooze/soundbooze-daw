## conversion 

```
sox -c 1 -r 22050 -i in.out out.wav
```

## Bit conversion

```
sox -b 16 in.out out.wav  
ffmpeg -i movie.mp4 -ss 00:00:03 -t 00:00:08 -async 1 cut.mp4
```

## trim

```
sox input.wav output.wav trim 10 20
```

## capture

```
jack_capture -d 11 -p system:capture* -f wav out.wav
```

## normalize

```
sox --norm=-1 in.wav out.wav
```

- http://billposer.org/Linguistics/Computation/SoxTutorial.html
