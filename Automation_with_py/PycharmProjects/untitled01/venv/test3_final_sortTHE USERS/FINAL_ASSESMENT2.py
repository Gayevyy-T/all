#!/usr/bin/env python3

import re, os, csv, sys, operator

error_message = {}
entries_number = {}

pattern = r"(ticky:) (INFO|ERROR) (\w.*) (\(\w.*\))"

with open("syslog.log", "r") as log:
    for line in log.readlines():
        match =  re.search(pattern, line)
        inf_err = match[2]
        username = match.group(4).strip().replace("(", "").replace(")", "")
        information = match[3]

        if inf_err == "INFO":
            entries_number[username] = entries_number.get(username, {"INFO": 0, "ERROR": 0})
            entries_number[username]["INFO"] += 1

        if inf_err == "ERROR":
            error_message[information] = error_message.get(information, 0) +1
            entries_number[username] = entries_number.get(username, {"INFO": 0, "ERROR": 0})
            entries_number[username]["ERROR"] += 1

error_sorted = sorted(error_message.items(), key=operator.itemgetter(1), reverse=True)
user_sorted = sorted(entries_number.items())

#result = []

#for user in user_sorted:
#    result.append((user[0],user[1]['INFO'], user[1]['ERROR']))

with open("error_message.csv", "w") as error:
    writer = csv.writer(error)
    writer.writerow(['Error','Count'])
    writer.writerows(error_sorted)

with open("user_statistics.csv", "w") as number:
    writer = csv.writer(number)
    writer.writerow(['Username', 'INFO', 'ERROR'])
#    writer.writerows(result)
    for user in user_sorted:   #not needed in case of 2d option
        writer.writerow((user[0],user[1]['INFO'], user[1]['ERROR']))