#! /usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import os
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    #Change this to your rookit's ip address
    port = 12345
    #Same as the port in the server1.py file
    s.connect((host,port))
    while True:
        dumm = ""
        try:
            s.send(input("message:").encode("utf-8"))
            dumpstt = []
            while True:
                dumpstr = s.recv(1024).decode("utf-8")
                if dumpstr[-3:] == "bbb":
                    dumpstt.append(dumpstr[:-3])
                    break
                else:
                    dumpstt.append(dumpstr)
            dumm = dumm.join(dumpstt)
        except Exception as e:
            dumm = str(e)
        print(dumm)
    pass
if __name__ == "__main__":
    main()