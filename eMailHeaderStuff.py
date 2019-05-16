#!/usr/bin/env python3

# import required modules
from __future__ import print_function
import re
import argparse
import os
import sys
from netaddr import *
import pprint
import socket

# clear screen
os.system('clear')


# title and space
print("")
print("       |  ---Email Stuff---  |       ")
print("       |    --By Daniel--    |      ")


# create a variable for the header
# read the header
# print header (for testing only. Will remove, or create an option to view.)
print("")
eMailHead = input("Header to import: ")
f = open(f"{eMailHead}","r")
caca = f.read()
#print(caca)


# Create a function that will grab email addresses from the header
def getAddresses():
    print("")
    print("List of extracted email addresses:")
    exampleString = caca
    eMails = re.findall(r'[\w\.-]+@[\w\.-]+',exampleString)
    dups = set(eMails)
    for email in dups:
        if email not in dups:
            email.append(email)
            seen.add(email)
            return eMails
        print(f"[+] {email}")
    print("")


# Create a function that will grab IPs and disregard any privates or loopbacks
def getIPs():
    print("List of extracted IP addresses:")
    exampleString = caca
#    IPsGot = re.findall(r'[\n\.-]+.[\n\.-]+',exampleString)
    IPsGot = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',exampleString)
    dups = set(IPsGot)
    for ipAddy in dups:
        if ipAddy not in dups:
            email.append(ipAddy)
            seen.add(ipAddy)
            return ipAddy
        try:
            socket.inet_aton(ipAddy)
            # filter out IP addresses we don't need
            meow = IPAddress(ipAddy).is_private() ; mew = IPAddress(ipAddy).is_loopback()
            if meow != True:
                if mew != True:
                    print(f"[+] {ipAddy}")
        except socket.error:
            ()
    print("")




getAddresses()
getIPs()
