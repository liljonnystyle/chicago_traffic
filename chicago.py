#!/usr/bin/python

from bs4 import BeautifulSoup as BS
import mechanize
from datetime import datetime
import sched, time

def scheduler(s):
	print time.time()
	s.enter(600, 1, get_csv, ())
	s.run()

def get_csv():
	url = 'https://data.cityofchicago.org/api/views/t2qc-9pjd/rows.csv?accessType=DOWNLOAD'

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('user-agent','Mozilla')];
	htmlfile = browser.open(url)

	htmltext = str(BS(htmlfile))

	start = 101 - htmltext[100::-1].index('>')
	end = htmltext[-100:-1].index('\n')-100

	now = datetime.now()
	ymd = now.strftime('%Y%m%d')
	time = now.strftime('%X')
	hr = time[0:2]
	mn = time[3:5]
	filename = 'data/' + ymd + hr + mn + '.csv'
	file = open(filename,'w')
	file.write(htmltext[start:end])

def main():
	s = sched.scheduler(time.time, time.sleep)
	get_csv()
	while True:
		scheduler(s)

if __name__ == '__main__':
	main()
