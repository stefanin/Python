#!/usr/bin/python3


import sys
import telnetlib
import time
HOST = input("Insert ip address :")
username = input("username :")
password = input("password : ")
command = "sh run"
term = "term len 0"


cmd1 = "enable"
tn = telnetlib.Telnet(HOST)
tn.set_debuglevel(1)
time.sleep(2)
tn.read_until(b"Username: ") #user
tn.write(username.encode('ascii') + b"\n")
time.sleep(2)
tn.read_until(b"Password: ")# password
tn.write(password.encode('ascii') + b"\n")
time.sleep(2)
tn.write(term.encode('ascii') + b"\n")
tn.write(command.encode('ascii') + b"\n")
time.sleep(2)
tn.write(b"\n")
time.sleep(2)
tn.write(b"\n")
time.sleep(2)
tn.write(b"exit\n")
lastpost = tn.read_all().decode('ascii')
R=""
i=0
for row in lastpost:
    
    if row=="\n":
        print("('"+R.rstrip("\n")+"')")
        R=""
    R=R+row
        

#print(lastpost)
tn.close()