# -*- coding: utf-8 -*-

from imgurpython import ImgurClient
from ptt_crawler2 import crawler
import os

def upload_photo(image_path):
#     client_id = os.environ.get("client_id")
#     client_secret = os.environ.get("client_secret")
#     access_token = os.environ.get("access_token")
#     refresh_token = os.environ.get("refresh_token")
    client_id="71c37719f9ac27f"
    client_secre="d673c88340471b400a09d32dcf6357777955220f"
    access_token="657fa67ad11ed2e8d7d518e365de37d10b74aa15"
    refresh_token="68ca0b7355c987916d126384f830770f66f84217"
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