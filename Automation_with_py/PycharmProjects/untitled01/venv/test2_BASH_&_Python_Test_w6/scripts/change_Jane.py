#!/usr/bin/env python3

import sys
import subprocess

argument = open(sys.argv[1], "r")
for line in argument.readlines():
    old_substring = line.strip()
    new_substring = old_substring.replace("jane", "jdoe")
    subprocess.run(["mv", old_substring, new_substring])
argument.close()