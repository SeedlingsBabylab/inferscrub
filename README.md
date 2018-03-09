# inferscrub

figure out what regions of an audio file have been silenced.

## usage

#### find silent regions in wav files: 
```
$ python infer.py [dir_with_wavs]
```
it'll output a file called ```silences.csv``` with a list of all the regions.

#### find PI regions based on personal info comments in chas
First, make sure there's a directory called ```errors``` in the folder that you're running this script from. It will be dumping error diagnostics there. 
```
$ python get_pi_regions.py [dir_with_chas]
```

outputs a file called ```pi_regions.csv``` with a list of all the regions

<br>

### dependencies

This script depends on FFMpeg being on your ```$PATH``` somewhere. (```brew install ffmpeg``` should do the trick)