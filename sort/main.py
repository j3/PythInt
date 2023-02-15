# Importing modules
import linecache
import os
import time
import re

def sort(file):
    print("Sorting started")
    tic = time.time()
    fichiertxt = open("tosort/"+file, "r", encoding="utf8")
    flag = 0
    i = 0
    for line in fichiertxt:
        i = i + 1
        found = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
        if '@' in found.group(0):
            flag = 1
            line = i
            line_sec = linecache.getline("tosort/"+file, line)
            place(line_sec, file)
    if flag == 0:
        print('No email was found on '+'@'+'.')
    tac = time.time()
    print("Database sorted in " + time.strftime("%H:%M:%S", time.gmtime(tac-tic)) + ".")

def place(line_sec, filename):
    email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line_sec)
    if os.path.exists('sorteddbs/'+email.group(0)[0]+'/'+email.group(0)[1]+'/') == True:
        with open('sorteddbs/'+email.group(0)[0]+'/'+email.group(0)[1]+'/'+email.group(0)[0]+email.group(0)[1]+'.txt', 'a') as the_file:
            the_file.write(filename+': '+line_sec)

# https://github.com/SoikRs/PythInt