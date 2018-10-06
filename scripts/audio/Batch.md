## conversion 

```
sox -c 1 -r 22050 -i in.out out.wav
```

## Bit conversion

```
sox -b 16 in.out out.wav  
```

## trim

```
sox input.wav output.wav trim 10 20
```

## capture

```
jack_capture -d 11 -p system:capture* -f wav out.wav
```
