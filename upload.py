# -*- coding: utf-8 -*-

from imgurpython import ImgurClient
from ptt_crawler2 import crawler
import os

def upload_photo(image_path):
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    access_token = os.environ.get("access_token")
    refresh_token = os.environ.get("refresh_token")
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    album = None # can also enter an album ID here
    config = {
        'album': album,
    }
    print("Uploading image... ")
    with open(image_path, 'rb') as fd:
            image = client.upload(fd, config=None, anon=True)
            print("Done") 
            return image['link'] 

# if __name__ == "__main__":
#     find_param = {'q' : '生日'}
#     string = ['鞋子', '卡片', '手錶']
#     oldpath = crawler(string, find_param)
#     path = upload_photo(oldpath)
#     print(path)