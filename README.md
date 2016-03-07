##Flickr Grabber (有村架純の画像500枚を2秒で保存できるプログラム)

FlickrGrabber is a program for getting many images from Flickr.com in a few seconds.

FlickrGrabberは一回の操作でflickr.comから何枚もの写真をパソコンに取り込む事のできるプログラムです。

## Description
By using major python modules, the program can parse any images that you want to search up to 500. The multithreading module allows the user to save all the parsed images in a few seconds.

ごく一般的なpythonのモジュールを用いて、どんな画像でも一気に500枚まで取得する事ができます。Multithreadingモジュールを利用する事により、それらの写真を数秒で自分のパソコンに保存する事もできます。

## Demo

## Requirement
The following python modules are required to make sure that the program works.

以下のpythonモジュールをインストールされている事によって、正常にプログラムが作動します。

 - sys
 - os
 - shutil
 - threading
 - json
 - urllib, urllib2
 - re
 - Beautifulsoup4

Furthermore, this program uses flickr.photo.search API, therefore a flickr API key is required. You can create a key from [here](http://www.flickr.com/services/api/keys/).

加えて、このプログラムはflickr.photo.search APIを使用しているため。APIキーが必要となります。キーは[こちら](http://www.flickr.com/services/api/keys/)から取得する事ができます。

## Usage
1. Open Terminal and move to the directory of 'FlickrGrabber' folder.
2. Compile final.py (type ```$ python final.py```).
3. Follow the instruction in the program.
4. Choose the language (type ```e``` or ```j```).
5. Type the word that you want to search.
6. Type the number of images that you want (maximum 500).
7. Save the parsed images or not (type ```y``` or ```n```).

===

1. ターミナルを開いて'FlickrGrabber'のディレクトリまで移動して下さい。
2. final.pyを実行して下さい (```$ python final.py```)。
3. プログラムの指示に従って進めて下さい。
4. 言語を選択して下さい（```e```か```j```を入力）。
5. 検索したいワードを入力して下さい。
6. 表示したい枚数を入力して下さい。(半角数字で500まで)。
7. 保存するか否かを選択して下さい（```y```か```n```を入力）。

## Licence

[FlickrGrabber](https://github.com/ryoogata10/FlickrGrabber)

## Author

©[ryo.ogata](https://github.com/ryogata10). All Rights Reserved.
