#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Written by ryo.ogata
# University student studying in Japan
# 
# This is made for a school project.

# input		-> get the links and generate a HTML file
# process	-> create basic html tags and img tags with parsed images' links
# ouput		-> generate a HTML file with parsed images
def indexHTML(links):
	from bs4 import BeautifulSoup, Tag
	soup = BeautifulSoup()

	h = open('index.html', 'w')

	html 	= soup.new_tag('html', )
	head 	= soup.new_tag('head')
	meta	= soup.new_tag('meta', charset = "utf-8")
	title	= soup.new_tag('title')

	body	= soup.new_tag('body')


	soup.append(html)
	html.append(head)
	html.append(meta)
	html.append(title)
	title.append('Ryosuke Ogata | Final Project')

	html.append(body)

	# create img tags with image links as 'src'
	for srcs in links:
			w = "window.innerWidth"
			img		= soup.new_tag('img', src = srcs, width = '20%')
			html.append(img)

	h.write( soup.prettify() )
	