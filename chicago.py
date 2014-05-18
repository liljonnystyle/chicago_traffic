#!/usr/bin/python

import urllib
import urlparse
from bs4 import BeautifulSoup as BS
import mechanize
import re
import hashlib

def main():
	url = 'https://data.cityofchicago.org/api/views/t2qc-9pjd/rows.csv?accessType=DOWNLOAD'

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('user-agent','Mozilla')];
	htmlfile = browser.open(url)

	htmltext = str(BS(htmlfile))

	start = 101 - htmltext[100::-1].index('>')
	end = htmltext[-100:-1].index('\n')-100
	file = open('dl.csv','w')
	file.write(htmltext[start:end])

if __name__ == '__main__':
	main()
