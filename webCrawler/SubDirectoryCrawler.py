#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://"+url)
    except Exception: # requests.exceptions.ConnectionError
        pass
        #print("The domain you're looking for is not exist")

target_url="10.0.2.15" # google.com

with open("../../files-and-dirs-wordlist.txt","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response :
            print("[+] Discovered URL --> " + test_url)


