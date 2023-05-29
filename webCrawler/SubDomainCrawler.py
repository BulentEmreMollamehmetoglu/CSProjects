#!/usr/bin/env python

import requests
import time # to check how long my code runs
#from datetime import datetime
#start_time = datetime.now()
# do your work here

#url = "google.com"
def request(url):
    try:
        return requests.get("http://"+url)
    except Exception: # requests.exceptions.ConnectionError
        pass
        #print("The domain you're looking for is not exist")
target_url="google.com"
with open("subdomains-wordlist.txt","r") as file:
    length_of_file = (len(file.read().splitlines()))
    file.close()
    #print(length_of_file)
num_lines = 0
with open("subdomains-wordlist.txt","r") as file:

    for line in file:
        print(line)
        start_time = time.perf_counter()
        #print(start_time)
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        #inside_time = datetime.now()
        #print(inside_time)
        num_lines += 1
        end_time = time.perf_counter()
        #print(end_time)
        elapsed_time = int(end_time - start_time)
        percentage = (100 * (num_lines / length_of_file))
        print(f"percentange : {percentage}")
        if (percentage) > 5:
            print(f"[+] 5 Seconds passed and %{percentage} ")
            #print (f"%{percentage} ")
        if response:
            print("[+] Discovered subdomain --> " + test_url)
        else:
            print(f"percentange : {percentage}")
#end_time = datetime.now()
#print('Duration: {}'.format(end_time - start_time))
