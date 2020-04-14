# Author  	  -> Gotam Dahiya
# Project     -> Network Mapping using a Hexacopter
# Application -> Program is used to capture various network's qualities such as signal strength, link qualtiy and channel used for broadcasting.
# Supervising Professor -> Dr. Paresh Saxena, Department of CSIS, BITS Hyderabad
# Id No. -> 2017A7PS0223H

# This program is written to measure the signal strength of a wifi signal produced by a mobile phone or any router.

# It can be configured to obtain the signal strength from cellular data by changing the interface value. The ESSID, address, link quality, and signal strength are all derived from the command line interface tool iwconfig/iwlist/iw.

# This program currently finds WiFi networks above a signal strength of -80dBm. It gives the channels, ESSIDs, Access point, Signal level, and Link quality of the network.

# Passive/Active scanning is used to hunt for networks.
# Passive scanning -> Process of scanning channels and listening for beacon frames.
# iwlist also uses active scanning when the interface is RFMODE, i.e., receiving network from an AP.
# Active  scanning -> Broadcasting a probe frame that will be received by access point within the wireless host's range.

# subprocess.check_output(['iwlist','<interface_name>','scan']) 		 -> iwlist
# subprocess.check_output(['iwconfig','<interface_name>'])       		 -> iwconfig   
# subprocess.check_output(['sudo','iw','dev','<interface_name>','scan']) -> iw [needs root password][obtain from different script file or store in this file directly]

# Signal level is calculated by taking logarithmic of the power of the signal to the base 10 . Here power is represented in milliWatts. The value obtained is negative
# x dBm = 10*log(P/(1 mW))
# P -> Power of signal/network
# Eg :- -10dBm = 0.1 mW  

# cv.waitKey(1) & 0xFF does not work currently for some reason. It used to terminate the main while loop to end the data recording.
# a try-catch statement with exception set to KeyboardInterrupt was tested which did not yeild any results. The exception was never caught by the program.

import serial
import re
import subprocess
import time
import os
import cv2 as cv
from pynmea import nmea
# from decimal import *

file="./log/data.log"
f=open(file,'w')
f.write("\n")
f.flush()
os.fsync(f)

# output lists
signal_level = [] # signal level of networks
essids = [] # ESSID of networks
link_quality = [] # Link quality of networks
address = [] # Access Point(AP) of network. IPv6 address of device broadcasting the networks
channel_no = [] # Channel on which it being received by user

print ("Reading Data")
print("Press ESC or Ctrl-C/Z to stop reading data") # Currently not working

while 1:
	# delete previous entries so that they are not repeated.
	del signal_level[:]
	del essids[:]
	del link_quality[:]
	del address[:]
	del channel_no[:]

	data=False
	while not data:
		try:
			# 'output' collects the data from the command line using subprocess library. 
			# CLI commands which can be used are iwlist, iwconfig, and iw. For iw "sudo" needs to be issued from the script which is not reccommened due to security issues.
			# wlo1 can be changed to the interface name demanded by the user.
			output = subprocess.check_output(['iwlist','wlo1','scan'])
			output = output.splitlines()
			data = True
			pass
		except:
			# incase any network is not detected
			continue
		pass

	# output = output.decode('ASCII')
	# print (output)

	addr_obt = False
	for line in output:
		line = line.decode('ASCII') # decoding from byte-object to string in ASCII.
		# print (line)

		addr = re.search('Address: (..:..:..:..)',line) # Access Point
		if addr is not None:
			address.append(addr.group(1))
			addr_obt = True
		# else:
		# 	address = "NAN"
		# print(address)

		quality = re.search('Quality=(.*?)/70',line) # Link Quality
		if quality is not None:
			link_quality.append(quality.group(1))
		# else:
		# 	link_quality = "NAN"
		# print(link_quality)

		signal  = re.search('Signal level=(.*?) dBm',line) # Signal Strength
		if signal is not None:
			signal_level.append(signal.group(1))
		# else:
		# 	signal_level = "NAN"
		# print(signal_level)

		essid = re.search('ESSID:\"(.* ?)\"',line) # ESSID of network
		if essid is not None:
			essids.append(essid.group(1))
		# else:
		# 	essids = "NAN"
		# print(essids)

		channel = re.search('Channel:(.?)',line) # Channel number
		if channel is not None:
			channel_no.append(channel.group(1))
		# else:
		# 	channel_no = "NAN"
		# print(channel_no)
	
	for i,val in enumerate(address):
		# Currently writing to a log file. It can be modified to write to a CSV file too.  
		try:
			f.write(essids[i] +" "+address[i] +" "+link_quality[i] +" "+signal_level[i]+" "+channel_no[i])
			f.write('\n')
			f.flush()
			os.fsync(f)
			pass
		except Exception as e:
			raise e

	f.flush()
	
	# k = cv.waitKey(1) & 0xFF
	# if k==27:
	# 	break
# print("Read data. Please go to ./log/data.log to see the results")