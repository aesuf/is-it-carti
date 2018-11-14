import os
import re
from pathlib import Path

rootdir = "/Users/quintenrivers/Music/iTunes/iTunes Media/Music"
songs = set([])
write_file = Path('data/songs_added.md')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file != ".DS_Store" and re.search(".m4a$",file):
            songs.add(re.sub('^\d+[-\d]+\s','',re.sub('.m4a$',"",file)))

with open(write_file,'w') as FH:
    for song in songs:
        FH.write('+ ' + song +"\n")
