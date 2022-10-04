# Importing modules
import linecache
import os

def trier(file):
    print("Sorting started")
    fichiertxt = open("tosort/"+file, "r", encoding="utf8")
    flag = 0
    i = 0
    arob = '@'
    for line in fichiertxt:
        i = i + 1
        if arob in line:
            flag = 1
            line = i
            ligne = linecache.getline("tosort/"+file, line)
            place(ligne, file)
    if flag == 0:
       print('No email was found on '+arob+'.')

def place(ligne, filename):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if os.path.exists('sorteddbs/'+ligne[0]+'/'+ligne[1]+'/') == True:
        with open('sorteddbs/'+ligne[0]+'/'+ligne[1]+'/'+ligne[0]+ligne[1]+'.txt', 'a') as the_file:
            the_file.write(filename+': '+ligne)

# https://github.com/SoikRs/PythInt