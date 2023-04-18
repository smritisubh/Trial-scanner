#!/bin/Python3

import sys
import socket 
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("invalid number of arguments")
	print("syntax: python3 port.py <ip>")	
	
print("-" *80)
print("scanning target: "+target)
print("time started: "+str(datetime.now()))
print("-" *80)

try:
	for port in range(50,500):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open")
		s.close()
			
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Host name is invalid.")
	sys.exit()
	
except socket.error:
	print("Could not reach to server.")
	sys.exit()					
			
			
						
