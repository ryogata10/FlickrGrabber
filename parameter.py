#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Written by ryo.ogata
# University student studying in Japan
# 
# This is made for a school project.


# parameters required to access to 'flick.photo.search' API.
# definition of each parameter can be see at
# -> https://www.flickr.com/services/api/flickr.photos.search.html

parameter = {
'api_key': '13375e9d61bdb942b64990b56ccf9e25',
'method': 'flickr.photos.search',
'sort': 'relevance',
'format': 'json',
'per_page': 20,
'nojsoncallback': 1,
'extras':'url_o',
'text': 'text input will be inserted'
}
