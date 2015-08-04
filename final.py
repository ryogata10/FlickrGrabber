#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Written by ryo.ogata
# University student studying in Japan
# 
# This is made for a school project.
# 
# The general feature of the function
# -> Parse the images from 'www.Flickr.com' using 'flickr.photo.search' API.
# -> User can easily decide the parameters by just typing simple words and numbers.
# -> Developers can also easily modify the program and adjust the parameters as they want.
# -> It generates a HTML file with parsed images, 
# and users can even save them on their own local environment.

# import all the files and functions from .py files in the directory
from photo import photoLink, savePic
from parameter import parameter
from tag_generator import indexHTML

# used for error notifications
import sys
# used for searching paths and creating directory
import os, shutil
# used for multithreading
import threading

# path to the current directory
path = (os.getcwd())

print 'Choose the language, either English or Japanese. (e/j)'
lang_input = raw_input()

# continue with the process unless something else than e or j is typed
if lang_input == 'e':
	text_q		= 'What do you want to search?'
	number_q	= 'How many images do you want?(integers only)'
	save_q		= 'Do you want to save the images? (y/n)'
	save_err	= 'Please type either \'e\' or \'j\''
	saving 		= 'Saving images...'
	parse		= 'Parsing images...'
	parse_comp 	= 'Processed successful!'
	finish		= 'Finished!\nImages are saved in \'' + path + '/img/\''
elif lang_input == 'j':
	text_q		= '検索したいワードを入力して下さい'
	number_q	= '画像を何枚取り込みたいですか？(半角英数字)'
	save_q		= '今回取り込んだ画像を保存しますか？(y/n)'
	save_err	= 'y か n でお答え下さい'
	saving		= '画像を保存中...'
	parse		= '画像をパース中...'
	parse_comp 	= '画像が正常に抽出されました!'
	finish 		= '完了しました!\n画像は \'' + path + '/img/\' に保存されました!'
else:
	print 'Please type either \'e\' or \'j\''
	sys.exit(0)

print text_q
text_input = raw_input()
print number_q
number_input = input()

# Define the parameters for building the JSON file
parameter['text']		= text_input
parameter['per_page']	= number_input

# start parsing the pictures
print parse
photoLink()
# convert them into a single HTML file
l = photoLink()
indexHTML(l)
print parse_comp

print save_q
save_input = raw_input()

# process of whether save the images on your localhost or not
if save_input == 'y':
	print saving
	# if there is already a directory called 'img', delete it
	if os.path.isdir('img') == True:
		shutil.rmtree('img')
	os.mkdir('img')
	for link in l:
		t = threading.Thread(target = savePic, args = (link,) )
		t.start()
elif save_input == 'n':
	sys.exit(0)
else:
	print 
	sys.exit(0)

# declare the end of function
print finish
