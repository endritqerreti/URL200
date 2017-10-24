#!/usr/bin/python


#App Name    : URL200
#Author      : Endrit Qerreti
#Repo        : https://github.com/endritqerreti/URL200
#License     : MIT License
#Version     : 1.0.0


import requests
import csv
import sys
import time
from datetime import date

seconds = 2
path = 'urls.txt'

today = date.today()

f = open(path, 'r')
count = f.readlines()


app_name = """\n
#  .##..##.#####..##......####...####...####..
#  .##..##.##..##.##.........##.##..##.##..##.
#  .##..##.#####..##......####..######.######.
#  .##..##.##..##.##.....##.....##..##.##..##.
#  ..####..##..##.######.######..####...####..
"""
print(app_name)


appname ="A Simple URL Checker"
version = "#Version : 1.0.0"
license = "#License : MIT License"
coded_by ="#Coded by: Endrit Qerreti"
print(appname.center(45),"\n","\n",version,"\n",license,"\n",coded_by,"\n")




if len(count) == 0:
    file_status = sys.exit("URLS.txt is empty")
else:
    file_status="[OK]"


line = '----'
print(line[0] * 58, )
print ("| URL loaded :",len(count),'|','Date :', today,"| File status:",file_status, "|")
print(line[0] * 58)



options = [

'\nOPTIONS\n',
'[Y] - To start checking URLs',
'[N] - To exit the program',
'',
]


for option in options:
    print(option)


set_option = input("Type Y/y or N/n: ").lower().strip()

if set_option == 'y':
    print ("starting..")
elif set_option == 'n':
    sys.exit("Program closed")
else:
    sys.exit("wrong command")



results = csv.writer(open('results.csv', 'w'))
results.writerow(['URL', 'Response', 'Date :', today])


good_urls = csv.writer(open('good_urls.csv', 'w'))
good_urls.writerow(['URL', 'Response', 'Date :', today])


count = 0
good_url = 0
bad_url = 0


with open(path, 'r') as urls:
 for adresa in urls:
     count += 1
     time.sleep(seconds)
     print("\n")
     adresa = requests.get(adresa.strip())
     pergjigja = adresa.status_code
     results.writerow([adresa.url, pergjigja])
     print([count],"Checking : ", adresa.url ,"\n[-] Response : ",pergjigja)
     if pergjigja == 200:
         good_url += 1
         good_urls.writerow([adresa.url, pergjigja])
     else:
         bad_url += 1
         continue

def statusi():

    print("\nGood URLs (200 OK):",[good_url],"\n---", "\nBad URLs :",[bad_url],"\n---", "\nTotal URLs :",[count],"\n")

statusi()
