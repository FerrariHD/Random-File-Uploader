import os
import random
import shutil
import time
from datetime import datetime, date


startTime = datetime.now().time()
print("Script started. Start time: " + str(startTime))

srcpath = "D:/music/"
dstpath = "E:/music"

listoftracks = os.listdir(srcpath)
print(len(listoftracks))
print(listoftracks)

shufflecounter = 0
while True:
    shufflecounter += 1
    random.shuffle(listoftracks)
    needtorestart = False
    for i in range(len(listoftracks)-2):
        if listoftracks[i].split(' ', 1)[0].lower() != "the":
            if listoftracks[i].split(' ', 1)[0].lower() == listoftracks[i+1].split(' ', 1)[0].lower():
                print(listoftracks[i].split(' ', 1)[0])
                print(listoftracks[i+1].split(' ', 1)[0])
                needtorestart = True
                break
        else:
            if listoftracks[i].split(' ', 2)[1].lower() == listoftracks[i + 1].split(' ', 2)[1].lower():
                print(listoftracks[i].split(' ', 2)[1])
                print(listoftracks[i + 1].split(' ', 2)[1])
                needtorestart = True
                break
    if needtorestart:
        print("reshuffled")
        continue
    print(shufflecounter)
    break

print(len(listoftracks))
print(listoftracks)

for nameoftrack in listoftracks:
    print(str(listoftracks.index(nameoftrack) + 1) + "/" + str(len(listoftracks)) + ":")
    print(srcpath + nameoftrack)
    time.sleep(1)
    shutil.copy2(srcpath + nameoftrack, dstpath)

endTime = datetime.now().time()
print("Full script completed. End time: " + str(endTime))
print("Full script completed in: " + str(datetime.combine(date.min, endTime) - datetime.combine(date.min, startTime)))
