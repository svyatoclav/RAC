
# RAC - RandomAutoCut 

import random
import secrets
import os
import time
import cv2 # in cmd: "pip install opencv-python" 

PATH = r"F:\Videos\1" # path to folder (and subfolders) with videos 
cuts = 150 # number of cuts (clips) 
minl = 6 # min length of cut in frames (in 30 fps 1 frame = 33 milsec) 
maxl = 155 # max length of cut in frames (in 30 fps 60 frames = 2 sec) 
rdml = 20 # max random length of cut 
rdmlprob = 25 # random length probability 
realfps = 0 # frames per second (set when need REAL FPS, than also swap "videoFPS[rdmboth]" to "realfps" in line 78) 

def frames_to_TC (frames, fps):
    h = int(frames / (3600*fps)) 
    m = int(frames / (60*fps)) % 60 
    s = int((frames % (60*fps))/fps) 
    f = frames % (60*fps) % fps
    return ( "%02d:%02d:%02d:%02d" % ( h, m, s, f))

def viddur(filename):
    video = cv2.VideoCapture(filename)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    return frame_count

def vidfps(filename):
    video = cv2.VideoCapture(filename)
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.') # Find OpenCV version 
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
    return fps


print('start')
existEDLfiles = os.listdir(PATH)
files = [os.path.join(root, name)
        for root, dirs, files in os.walk(PATH)
            for name in files
                if name.endswith((".mov",".mp4",".m4v",".mts",".MP4", ".MOV", ".M4V", ".MTS"))]


# .edl count 
edlFiles = []
for i in range(0,len(existEDLfiles)):
    if existEDLfiles[i][-4:] == ".edl":
        edlFiles.append(existEDLfiles[i])
if (len(edlFiles) == 0): edlFiles.append("rac0.edl")
edlFiles.sort(key=lambda x: int(x[3:-4]))
edlFiles = [int(x[3:-4]) for x in edlFiles]
edlForPrint = (int(edlFiles[-1])+1)

# video names and length 
videoFiles = []
videoLength = []
videoFPS = []
for i in range (0, len(files)):
    videoFiles.append(files[i])
    videoLength.append(viddur(files[i]))
    videoFPS.append(vidfps(files[i]))

# random and writing to the file time(s) 
print('TITLE: 0 ',PATH,'\nFCM: NON-DROP FRAME\n', file=open(PATH + '\\' + "rac" + str(edlForPrint) + ".edl", "a+"))
i = 1
length = 0
print('\ncuts:',cuts,'\nminl:',minl,'\nmaxl:',maxl,'\nrdml:',rdml,'\nrdmlprob:',rdmlprob,'\n')
for U in range (0, cuts, 1):
    try: 
        ForMaxL = maxl
        rdmboth = random.randint(0, len(videoFiles)-1)
        rdmvid = videoFiles[rdmboth]
        srcin = secrets.randbelow(videoLength[rdmboth])
        fps = videoFPS[rdmboth] # "videoFPS[rdmboth]" or "realfps" 
        if (secrets.randbelow(100) < rdmlprob): # random short length of cut 
            ForMaxL = secrets.randbelow(rdml)+minl
        if (minl >= maxl): rdmLength = ForMaxL = minl
        else: 
            rdmLength = int(random.uniform(random.uniform(minl, ForMaxL-1), secrets.randbelow(ForMaxL)))
        if (rdmLength < minl): rdmLength = minl
        if (srcin+rdmLength > videoLength[rdmboth]): 
            srcin = 0
            if (videoLength[rdmboth]-1 > ForMaxL): rdmLength = ForMaxL 
            else: rdmLength = videoLength[rdmboth]-1 
        print(i,"  AX       B     C        ",frames_to_TC(srcin, fps)," ",frames_to_TC(srcin+rdmLength, fps)," ",frames_to_TC(length, fps)," ",frames_to_TC(length+rdmLength, fps),'\n* FROM CLIP NAME: ',rdmvid,'\n', sep="", file=open(PATH + '\\' + "rac" + str(edlForPrint) + ".edl", "a+"))
        i += 1
        length += rdmLength
    except: UnicodeEncodeError

print('\nfinal length:',frames_to_TC(length, fps))
print('final clips:',i-1)
print(fr"done in file: {PATH}\rac{edlForPrint}.edl")

# by Svyatoclav - dev test ver. 1.4.2 for Premiere Pro 11.10.2022 (also thx DZgas and ilyss) 
