import os
import imghdr
import re
from bs4 import BeautifulSoup



path = "blogpath/public"

imgpathdct = dict()

#search images
for dirpath,dirnames,filenames in os.walk(path):
    for i in filenames:
        if imghdr.what(dirpath+'/'+i):
            #print(dirpath, name)
            imgpathdct[i] = dirpath[len(path):] + '/' + i


#edit path
for dirpath, dirnames, filenames in os.walk(path):
    for i in filenames:
        name, ext = os.path.splitext(i)
        if ext==".html":
            soup = BeautifulSoup(open(dirpath+'/'+i))
            img_list = soup.find_all("img")
            for im in img_list:
                #print(im.get('src'))
                if im['src'] in imgpathdct:
                    im['src'] = imgpathdct[im['src']]
                    print(im['src'])
            with open(dirpath+'/'+i, 'w') as f:
                f.write(soup.prettify())
            print(dirpath+'/'+i + " finished")



