#!/usr/bin/python

import urllib
import urlparse
from bs4 import BeautifulSoup as BS
import mechanize
import re
import hashlib

def searchPic(name):
	img_list = getPic(name)
	if len(img_list) > 0:
		for img in img_list:
			savePic(name,img)

def getPic(name):
	img_urls = []
	try:
url = "https://data.cityofchicago.org/api/views/t2qc-9pjd/rows.csv?accessType=DOWNLOAD"
		url = "http://instagram.com/" + name
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders = [('user-agent','Mozilla')];
		#,('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
		htmlfile = browser.open(url)

		#htmlfile = urllib.urlopen(url)
		htmltext = str(BS(htmlfile))
		dataline = ''
		for line in htmltext.split("\n"):
			if line.find('low_resolution') > 0:
				dataline = line
				break
		start = "low_resolution\":{\"url\":\""
		end = "\","
		regex = start + "(?!.*" + start + ").*?" + end
		pattern = re.compile(regex)

		count = 0
		for image in dataline.split("\"images\""):
			if count > 0:
				url = re.findall(pattern,image)
				img_urls.append(url[0].replace(start,"").replace(end,"").replace("\/","/"))
			count += 1

		start = ":\""
		end = "\","
		regex = start + end
		pattern = re.compile(regex)

		count = 0
		for username in dataline.split("\"username\""):
			if count > 0:
				user = username.split("\"")[1]
				if user != name:
					add2queue(user)
			count += 1
	except:
		print 'error'
	return img_urls

def savePic(name,img):
	hs = hashlib.sha224(img).hexdigest()
	ext = img.split(".")[-1]
	if ext != 'mp4':
		dest = 'pics/' + hs + '_' + name + '.' + ext
		try:
			urllib.urlretrieve(img,dest)
		except:
			print 'save failed'

def add2queue(user):
	qfile = open('queue.txt','r+')
	users = qfile.readlines()
	testuser = user + '\n'
	if testuser not in users:
		qfile.write(user + '\n')
	qfile.close()

def main():
	user = 'liljonnystyle'

	qfile = open('queue.txt','w')
	qfile.write(user + '\n')
	qfile.close()
	usercount = 1

	searchPic(user)
	qfile = open('queue.txt','r')
	users = qfile.readlines()
	qfile.close()

	while usercount <= len(users)-1:
		if usercount > 1000: break
		user = users[usercount][0:-1]
		searchPic(user)
		usercount += 1
		qfile = open('queue.txt','r')
		users = qfile.readlines()
		qfile.close()

if __name__ == '__main__':
	main()
