import os
import imghdr
import re
from bs4 import BeautifulSoup



path = "../myblog/public"
pre_address = "https://raw.githubusercontent.com/wlxyz/wlxyz.github.io/master/"
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
                print(im.get('src'))
                im['src'] = im['src'].rsplit('/', 1)[-1]
                if im['src'] in imgpathdct:
                    im['src'] = pre_address + imgpathdct[im['src']]
                    print('edit' ,im['src'])
            with open(dirpath+'/'+i, 'w') as f:
                f.write(soup.prettify())
            print(dirpath+'/'+i + " finished")



