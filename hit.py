import urllib2 as u
from time import sleep, time
import os

pid = str(os.getpid())
url = 'url'
period = 120
file_path = "log_file_path"

def writedata(line):
    fp = open(file_path, "a")
    fp.writelines(line)
    fp.close()

writedata("\n\n---new--- : "+str(int(time()))+" : "+str(period)+"\n")

cur = time()
prev = 0

while True:
    cur = time()
    line = "."
    if cur-prev >= period:
        line = "\n"+pid+" : "+str(int(cur-prev))
        try:
            r = u.urlopen(url)
            line += " : Successful!\n"
        except Exception as e:
            line += ": Error : "+str(e)+"\n"
        prev = cur
    writedata(line)
    sleep(1)
