import moviepy.editor as mp
from os import listdir
from os.path import isfile, join

mypath = "."
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count = 1
total = len(onlyfiles)
for file in onlyfiles:
    print str(count) + "/" + str(total)
    if file[-3:]=='mp4':

        clip = mp.VideoFileClip(file)
        clip.audio.write_audiofile("mp3/"+file[0:-4]+".mp3")
    count +=1