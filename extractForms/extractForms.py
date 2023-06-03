#!/usr/bin/env python

import requests
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://10.0.2.4/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
forms_list = soup.findAll("form")

for form in forms_list:
    #print(form)
    action = form.get("action")
    post_url = urljoin(target_url,action)
    method = form.get("method")
    #print(post_url)
    inputs_list = form.findAll("input")
    post_data = {}

    for inputs in inputs_list:
        input_name = inputs.get("name")
        input_type = inputs.get("type")
        input_value = inputs.get("value")
        if input_type == "text":
            input_value = "test"
        #print(input_name)
        post_data[input_name] = input_value
    result = requests.post(post_url,data=post_data)
    soup2 = BeautifulSoup(response.content, 'html.parser')
    print(soup2.prettify())
#print(forms_list)
