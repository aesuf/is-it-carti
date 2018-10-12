# is-it-carti

## Song Processing Guide

1. Convert song to a .wav file using [sox](http://sox.sourceforge.net/)

2. Compute mfcc values for that song using the script `compute-mfcc` found [here](https://github.com/dspavankumar/compute-mfcc), using the following format:

> compute-mfcc --input <song.wav> --output <output.csv> --samplingrate 44100

See the script's README for compilation instructions.

3. For each coefficient, take the mean and standard deviation across all samples.

Then, compile all of the songs that you process into one main csv file, which can be pushed to the repository.

## Modeling

Make your own repository for working on the classification problem
