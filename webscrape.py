#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

doc = sys.argv[1]
req = requests.get(doc)

soup = BeautifulSoup(req.content, "html.parser")
section = soup.body

for string in section.strings:
    print(string)
