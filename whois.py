#!/usr/share/python3

import socket, sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org", 43))
s.send(sys.argv[1]+"\r\n")
response = s.recv(1024).split()
whois = response[19]
s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois, 43))
s1.send(sys.argv[1]+"\r\n")
response1 = s1.recv(1024)
print(response1)

