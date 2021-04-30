#!bin/python3
import sys
from datetime import datetime
import argparse #allows us to parse arguments
import socket
parser = argparse.ArgumentParser() #saves us typing time
parser.add_argument("ip",help="The target ip for scanning")
parser.add_argument("port",help="The port or port range you want to scan, give range in form '<start number>, <end number>'")
args = parser.parse_args() #also saves typing time

#Define our target for scanning
#when running python3 portscanner.py <ip>, the file portscanner.py is considered argument 0 for the command python3, so adding another argument increases the total args to 2, with ip being arg 1

target = socket.gethostbyname(args.ip) #translates name to IP address if given

#pretty banner stuff
print("-" * 50)
print('Scanning started at ' + str(datetime.now()))
print('ip ' + target + ' and port(s) ' + args.port)
print("-" * 50)

#determines if single port or multiple ports 
try:
	ports = int(args.port)
except:
	ports = range(int(args.port.split(',')[0]),int(args.port.split(',')[1]))

#the actual scanning part
try:
	for x in ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET is ipv4 calling, sockstream is for ports
		socket.setdefaulttimeout(1) #sets time out time
		result = s.connect_ex((target,x)) #returns an error indicator is something goes wrong, else returns 0
		print("checking port {}".format(x))
		if result == 0:
			print("port {} is open!".format(x))
	s.close() #closes connection for that port

#exceptions
except KeyboardInterrupt: #if CTRL+C pressed
	print:('\n Scan aborted')
	sys.exit()

except socket.gaierror: #if error in connection
	print ('hostname could not be resolved')
	sys.exit()

except socket.error: #if connection impossible
	print ('Could not connect to ip')
	sys.exit()

finally:
	print("-" * 50)
	print('scanning complete at {}'.format(str(datetime.now())))
	print("-" * 50)

			

