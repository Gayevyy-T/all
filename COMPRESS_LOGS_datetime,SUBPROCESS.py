 #==============WONDOWS======================   
import datetime, os, sys
import subprocess

path = os.listdir('C:\\Users\\A645674\\Desktop\\Atom\\test\\')
full_path = 'C:\\Users\\A645674\\Desktop\\Atom\\test\\'

now = datetime.date.now()    #with hours
today = datetime.date.today()    #only date
two_days = datetime.timedelta(days=2)  #2 days could be added or takken

for file in path:
    if 'Text' in file:
        print(subprocess.run(['compact', full_path + file], shell=True))

 #==============LINUX======================        
#!/usr/bin/env python2
# OR USE PYTHON3 IN CASE IF VERSION 3 IS INSTALLED

import os
import subprocess

#now = datetime.date.today()       #not needed in my case
#two = datetime.timedelta(days=2)

path = os.listdir('/root/folder')
full_pah = '/root/folder/'

for file in path:
    if file.endswith('.log'):
        continue
    if file.endswith('xz'):
        continue
    else:
#        print(subprocess.run(['xz', full_pah + file]))  #Python3
        print(subprocess.call(['xz', full_pah + file]))  #Python2
#===============================================================
#http://www.pressthered.com/adding_dates_and_times_in_python/
#https://www.programiz.com/python-programming/datetime


temporaryunemployment-stdout.log.2020-10-27_0015 temporaryunemployment-stdout.log.2020-10-27_0131 temporaryunemployment-stdout.log.2020-06-04_0803 temporaryunemployment-stdout.log.2020-06-18_1017 temporaryunemployment-stdout.log.2020-07-13_1117 temporaryunemployment-stdout.log.2020-08-04_1118.xz temporaryunemployment-stdout.log.2020-10-03_1818.xz temporaryunemployment-stdout.log.2020-10-15_0139.xz
