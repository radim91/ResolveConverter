#!/usr/bin/env python3
import os, sys
import subprocess

SELECTED = []

def Converting():
    OPTIONS_D = ["D", "d", "davinci", "resolve", "Davinci", "Resolve"]
    OPTIONS_M = ["M", "m", "mp4", "MP4"]
    VERSION = input("What is your desired format?\n-------\n[D]avinci Resolve | [M]p4 : ")
    if str(VERSION) in OPTIONS_D:
        usage = "davinci"
        print("-------")
        return usage
    elif str(VERSION) in OPTIONS_M:
        usage = "mp4"
        print("-------")
        return usage
    elif str(VERSION) not in OPTIONS_D or OPTIONS_M:
        print("-------\nPlease respect, that you have to type \"D\" or \"M\".")
        raise(IOError)

def FormattedDict(dictionary):
    print("")
    for i in dictionary:
        print(" {}: {:>45.55}\t".format(i, dictionary.get(i)))        

def DirectoryList(path):
    DIRS = os.listdir(path)
    INDEX = 1
    TYPES = (".mp4", ".mov", ".avi", ".mkv")
    DICTIONARY = {}
    for i in DIRS:
        if i.endswith(TYPES):
            DICTIONARY.setdefault(INDEX,i)
            INDEX += 1
    FormattedDict(DICTIONARY)
    select = input("\nSelect a file to convert (type \"a\" to select all of them): ")
    if select.lower() == "a":
        for i in DICTIONARY:
            SELECTED.append(DICTIONARY[i])
    else:
        CONT = True
        while CONT == True:  
            if int(select) <= len(DICTIONARY):
                SELECTED.append(DICTIONARY.get(int(select)))
                print("Your list: ", SELECTED)
                select = input("------\nSelect a file to convert: ")
                CONT = True
            if not select:
                CONT = False
    print("\nYour list of selected videos:", SELECTED, "\n------")

def CreateConvertedDir(path):
    DIRS = os.listdir(path)
    conv_path = path + "/converted/"
    if "converted".lower() in DIRS:
        return True
    elif "converted".lower() not in DIRS:
        subprocess.run(["mkdir", conv_path])
        return True
    else:
        return SystemError

converting = Converting()
path = input("Which directory should I scan for files? (default = ./): ")
if path == "":
    path = os.getcwd()
DirectoryList(path)
CreateConvertedDir(path)
if converting is "davinci":
    for i in SELECTED:
        i_new = i[:-3] + ".mov"
        conv_path_obj = path + "/" + i
        conv_path = path + "/converted/" + i_new
        subprocess.run(["ffmpeg", "-i", conv_path_obj, "-c:v", "dnxhd", "-profile:v", "dnxhr_hqx", "-pix_fmt", "yuv422p10le", "-c:a", "pcm_s16le", conv_path])
elif converting is "mp4":
    for j in SELECTED:
        j_new = j[:-3] + ".mp4"
        conv_path_obj2 = path + "/" + j
        conv_path2 = path + "/converted/" + j_new
        subprocess.run(["ffmpeg", "-i", conv_path_obj2, "-f", "mp4", "libx264", "-preset", "medium", "-acodec", "aac", conv_path2])
else:
    print("Something went wrong.")

print("\n-------\nThank you for using the program. (c) Radim Hejduk 2019")
