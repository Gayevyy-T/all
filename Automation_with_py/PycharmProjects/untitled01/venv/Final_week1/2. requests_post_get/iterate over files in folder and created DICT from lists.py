#!/usr/bin/env python3

import os, requests

keys = ["title", "name", "date", "feedback"]
list = []
path = "/data/feedback/"

for file in os.listdir(path):
    dict = {}
    keycount = 0
    with open(path + file) as content:
        for line in content:
            formated = line.strip()
            dict[keys[keycount]] = formated
            keycount += 1
        list.append(dict)

    response = requests.post("http://35.188.79.160/feedback/", json=dict)
print(response.request.body)
print(response.status_code)
