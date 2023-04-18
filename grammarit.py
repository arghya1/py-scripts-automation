#!/usr/bin/python3

# pip install gingerit

import gingerit.gingerit as ginger

text = "dis is an sentence that ahs no future"

grammer = ginger.GingerIt()
result = grammer.parse(text)

# Original text
print(result['text'])

# Corrected text
print(result['result'])
