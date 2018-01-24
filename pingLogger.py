# -*- coding: utf-8 -*-
"""
@author: Sebastià
"""
from time import gmtime, strftime, time, sleep
import datetime
import csv
import os

def getLastPing(filename):
	with open(filename) as file:
		return file.read()

def deleteFile(filename):
	try:
	    os.remove(filename)
	except Exception as e:
		print(e)

def storeFile():
	myFile = open("dataloggers.csv", 'w')
    with myFile:
        writer = csv.writer(myFile, delimiter=';')
        for row in lines:
        	writer.writerow(row)
        

basePath = "/home/pi/FTP/pings"

for fname in os.listdir(basePath)
    path = os.path.join(basePath, fname)
    pingReceived = False
    with open('dataloggers.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimeter=',')
    	lines = [l for l in readCSV]
    	rownum = 0
    	for row in lines:
    		if lines[rownum][0] == fname
    			try:
    				lines[rownum][1] == getLastPing(fname)
    			except Exception as e:
    				print(e)
    			else:
    				pingReceived = True
    				deleteFile(fname)
    		rownum=rownum+1
    	if pingReceived == False
    		try:
    			lastPing == getLastPing(fname)
    		except Exception as e:
    			print(e)
    		else:
    			pingReceived = True
    			lines.append([fname, lastPing])
    			deleteFile(fname)

   


    