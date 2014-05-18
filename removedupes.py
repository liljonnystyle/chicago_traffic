#!/usr/bin/python

import os, sys

path = 'data/'
dirs = os.listdir(path)

dirs = sorted(dirs)

for file in dirs:
	try:
		file1 = open(path+oldfile,'r')
		file2 = open(path+file,'r')
		lines1 = file1.readlines()
		lines2 = file2.readlines()
		if lines1 == lines2:
			os.remove(path+file)
			print 'removing ' + file
		else:
			oldfile = file
	except:
		oldfile = file
