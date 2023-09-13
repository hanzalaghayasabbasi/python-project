#!/usr/bin/python3

import sys
import socket
import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translating hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 portscanner.py <ip>")
    sys.exit()

print("Scanning target " + target)
print("Time started: " + str(datetime.datetime.now()))

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # error indicator

        if result == 0:
            print('Port {} is open'.format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to the server.")
    sys.exit()


