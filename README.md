# inferscrub

figure out what regions of an audio file have been silenced.

## usage

```
$ python infer.py [dir_with_wavs]
```
it will output a file called ```silences.csv``` with a list of all the regions.

#### dependencies

This script depends on FFMpeg being on your ```$PATH``` somewhere. (```brew install ffmpeg``` should do the trick)