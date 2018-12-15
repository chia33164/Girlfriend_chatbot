from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_button_message
from utils import send_image_url
from ptt_crawler2 import crawler
from upload import upload_photo

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    # for choose
    def is_going_to_choose(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'start'
        return False
    
    def on_enter_choose(self, event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你女朋友怎麼了嗎？")

    # for birthday
    def is_going_to_birthday(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'birthday'
        return False
    
    def on_enter_birthday(self, event):
        sender_id = event['sender']['id']
        find_param = {'q' : '生日'}
        string = ['鞋子', '卡片', '手錶']
        old_img_url = crawler(string, find_param)
        img_url = upload_photo(old_img_url)
        btn = [
            {
              "type": "postback",
              "title": "鞋子",
              "payload": "鞋子"
            },
            {
              "type": "postback",
              "title": "手錶",
              "payload": "手錶"
            },
            {
              "type": "postback",
              "title": "卡片",
              "payload": "卡片"
            }
        ]
        send_text_message(sender_id, "網路推薦禮物前三名")
        send_image_url(sender_id, img_url)
        send_button_message(sender_id, "請選擇一個", btn)

    # for angry
    def is_going_to_angry(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'angry'
        return False

    def on_enter_angry(self, event):
        sender_id = event['sender']['id']
        find_param = {'q' : '生氣'}
        string = ['放生', '道歉', '禮物']
        old_img_url = crawler(string, find_param)
        img_url = upload_photo(old_img_url)
        btn = [
            {
              "type": "postback",
              "title": "放生",
              "payload": "放生"
            },
            {
              "type": "postback",
              "title": "道歉",
              "payload": "道歉"
            },
            {
              "type": "postback",
              "title": "禮物",
              "payload": "禮物"
            }
        ]
        send_text_message(sender_id, "網路推薦方式前三名")
        send_image_url(sender_id, img_url)
        send_button_message(sender_id, "請選擇一個", btn)

    # for month
    def is_going_to_month(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'month'
        return False
    
    def on_enter_month(self, event):
        sender_id = event['sender']['id']
        find_param = {'q' : '月經'}
        string = ['巧克力', '不理', '黑糖']
        old_img_url = crawler(string, find_param)
        img_url = upload_photo(old_img_url)
        btn = [
            {
              "type": "postback",
              "title": "巧克力",
              "payload": "巧克力"
            },
            {
              "type": "postback",
              "title": "不理",
              "payload": "不理"
            },
            {
              "type": "postback",
              "title": "黑糖",
              "payload": "黑糖"
            }
        ]
        send_text_message(sender_id, "網路推薦法寶前三名")
        send_image_url(sender_id, img_url)
        send_button_message(sender_id, "請選擇一個", btn)

    # for happy
    def is_going_to_happy(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return (text == '巧克力')|(text == '黑糖')|(text == '卡片')|(text == '鞋子')|(text == '手錶')|(text == '禮物')|(text == '道歉')
        return False

    def on_enter_happy(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜你度過這次難關")
        self.go_back()

    # for bad end
    def is_going_to_bad(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return (text == '不理')|(text == '放生')
        return False

    def on_enter_bad(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "死去")
        self.go_back()