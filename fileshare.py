#!/usr/bin/python3

# File Storage
# pip install gofile

import gofile as gof
import sys

file = sys.argv[1]

def store_files(file):
    cur_server = gof.getServer()
    print(cur_server)
    url = gof.uploadFile(file)
    print("Download Link: ", url["downloadPage"])
store_files(file)
