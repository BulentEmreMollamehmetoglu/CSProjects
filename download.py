#!/usr/bin/env python

import requests

def download(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(response.content)
    with open(file_name,"wb") as file:
        file.write(response.content)
download("https://cdn.motor1.com/images/mgl/rMjOr/s1/2022-nissan-gt-r-nismo-special-edition.jpg")
