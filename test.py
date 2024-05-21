#!/usr/bin/python3
import re

string = "yay {brahim sarouri} yoy"

pattern = r'\{[^}]*\}'
extracted_striny = ""
found = 0
if re.search(pattern, string):
    for c in string:
        if c == '{':
            found += 1
        if found == 1:
            extracted_striny += c
            if c == '}':
                break
else:
    print("doesn't match")
print(extracted_striny)
