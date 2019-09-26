#!/usr/bin/env python

# this will (hopefully) grab out all IP's in a text file
# can be useful for snatching asshole IP's from system logs
# expecially auth.logs and daemonlogs
# still a work in progress, with enhancements and other features to come.
# nh

# import python regular expression module
import re

# define function that will grab ip's and print them
def grabIP():
     ip_file = open("ip.txt")
     showMe = ip_file.read()
     ip_file.close()
     listIP = re.findall(r'(?<=)\d{1,3}(?:\.\d{1,3}){3}(?=)+', showMe,re.MULTILINE)
     print(listIP)

# run the function
grabIP()
