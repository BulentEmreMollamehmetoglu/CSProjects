'''
with open("../subdomains-wordlist.txt","r") as file:
    len_of_file = (len(file.read().splitlines()))
    file.close()
total = len_of_file
num_lines = 0
for line in open("../subdomains-wordlist.txt"):
    num_lines += 1
    percentage = int(100 * num_lines / total)
    print (f"%{percentage} ")
'''
'''
import time

# Start timer
start_time = time.perf_counter()

# Code to be timed
# ...
time.sleep(6)
# End timer
end_time = time.perf_counter()

# Calculate elapsed time
elapsed_time = int(end_time - start_time)
if (elapsed_time%10) > 5:
    print("5 seconds passed")
print("Elapsed time: ", elapsed_time)
'''

'''
import requests
def request(url):
    try:
        return requests.get("http://google.com")
    except Exception: # requests.exceptions.ConnectionError
        pass
        #print("The domain you're looking for is not exist")
'''
import subprocess

with open("../../files-and-dirs-wordlist.txt","r") as file:
    file_name_list = file.read().splitlines()
executed_files_list = file_name_list[300:400]
for file_name in executed_files_list:
    subprocess.run("sudo mkdir /var/www/html/"+ file_name,shell=True)
