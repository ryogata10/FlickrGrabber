#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Written by ryo.ogata
# University student studying in Japan
# 
# This is made for a school project.

# 'parameter.py' file
from parameter import parameter
# JSON and url-generating
import json, urllib, urllib2
# error notification
import sys
# used for regular expressions
import re
# used for creating directory and getting paths
import os
import threading

# input		-> dictionary with single key and value
# example_of_dictionary = {
# 	'key' : 'value',
# 	'key2' : 'value2'
# }
# process	->	get 'key' and 'value' and join them together
# output	-> 'k=v&k=v&k=v&k=v&k=v'
def objectQuery(obj):
	list = []
	for key, value in obj.items():
		k = urllib.quote(key, safe='~()*!.\'')
		v = urllib.quote(str(value), safe='~()*!.\'')
		list.append(k + '=' + v)
	query = '&'.join(list)
	return query

# input		-> none
# process	-> get the link (url) and read it as a JSON file
# output 	-> https://farm{farm}.staticflickr.com/{server}/{id}_{secret}.jpg
def photoLink():
	url = 'https://www.flickr.com/services/rest/?' + objectQuery(parameter)
	# print url

	r = urllib2.urlopen(url)
	load = json.load(r)

	# check if the JSON file is read correctly
	if load.get('photos') is None:
		sys.exit('Oops! Couldn\'t get the JSON file properyly. Please check the parameters!' +\
			'\nJSONファイルが正常に取得できませんでした。パラメータに正しく選択されているか確認してみてください')

	photo = load['photos']['photo']

	# get the links and add them into a list
	list = []
	for link in photo:	
		try:
		 	link.get('url_o')
			url = link['url_o']
		except KeyError:
			# sample image if the parsed image is unavailable
		 	url = 'http://img1.wikia.nocookie.net/__cb20141028171337/pandorahearts/images/a/ad/Not_available.jpg'
			
		list.append(url)
	return list

# input		-> get the list of links
# process	-> open the link and save its content as '.jpg'
# output	-> directory called 'img' with parsed images saved
def savePic(link):
	# save images
	path = ( os.getcwd() ).decode('utf-8')
	new_src = re.findall('\w+(?=.jpg)', link.encode('utf-8') )
	string_src = str(new_src)
	sub_src = re.sub('[\[\'\]]', '', str(new_src) )
	string_src = str(sub_src)
	fp = urllib2.urlopen(link)
	# open the link as a localhost file on your computer
	local = open( path + '/img/' + string_src + '.jpg', 'wb');
	# write (create the 'jpg' file)
	local.write(fp.read());
	local.close()
	fp.close()
