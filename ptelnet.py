#!/usr/bin/python3


import sys
import telnetlib
import time
import socket

class ptelnet:
    HOST=""
    UserName=""
    Password=""
    PasswordTelnet=""
    EnaUser=""
    EnaPassword=""
    T=telnetlib.Telnet()

    def __init__(self,HOST,UserName="",Password="",PasswordTelnet="",EnaUser="",EnaPassword="",debug=0):
        self.HOST=HOST
        self.Username=UserName
        self.Password=Password
        self.PasswordTelnet=PasswordTelnet
        self.EnaUser=EnaUser
        self.EnaPassword=EnaPassword
        self.T.host=HOST        
        self.T.set_debuglevel(debug)# 0=none 1=debug

    

    def LoginCisco(self):
        if UserName!="":
            self.T.read_until(b"Username: ")
            self.T.write(self.UserName.encode('ascii')+b"\n")
            time.sleep(2)
            self.T.read_until(b"Password: ")
            self.T.write(self.Password.encode('ascii')+b"\n")
            time.sleep(2)
            self.Write("term len 0")
            time.sleep(2)
    
    def Write(self,stringa=""):
        comando="sh run "
        self.T.write(comando.encode('ascii') + b"\n")
        print(comando)
        time.sleep(2)
    
    def Read(self):
        return self.T.read_all().decode('ascii')
        

    def Close(self):
        self.T.close()

    

HOST = "172.31.244.7"
username = "prada"
password = input("password : ")
tn1=ptelnet(HOST,username,password,debug=1)
tn1.Write("sh run")
tn1.Close()
print(tn1.Read())

