from transitions.extensions import GraphMachine
import os, sys
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
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'start'
        return False
    
    def on_enter_choose(self, event):
        sender_id = event['sender']['id']
        btn = [
            {
              "type": "postback",
              "title": "她生日快到了\n該送什麼禮物給她",
              "payload": "她生日快到了\n該送什麼禮物給她"
            },
            {
              "type": "postback",
              "title": "她月經來了，我該怎麼辦",
              "payload": "她月經來了，我該怎麼辦"
            },
            {
              "type": "postback",
              "title": "她正在生氣...，我該怎麼辦",
              "payload": "她正在生氣...，我該怎麼辦"
            }
        ]
        send_button_message(sender_id, "你女朋友怎麼了嗎？", btn)

    # for birthday
    def is_going_to_birthday(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '她生日快到了，該送什麼禮物給她'
        return False
    
    def on_enter_birthday(self, event):
        sender_id = event['sender']['id']
        find_param = {'q' : '生日'}
        string = ['鞋子', '卡片', '手錶']
        Estring = ['shoes', 'watch', 'card']
        old_img_url = crawler(string, find_param, Estring)
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
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '她正在生氣...，我該怎麼辦'
        return False

    def on_enter_angry(self, event):
        sender_id = event['sender']['id']
        find_param = {'q' : '生氣'}
        string = ['放生', '道歉', '禮物']
        Estring = ['not care', 'say sorry', 'gift']
        old_img_url = crawler(string, find_param, Estring)
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
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '她月經來了，我該怎麼辦'
        return False
    
    def on_enter_month(self, event):
        sender_id = event['sender']['id']
        find_param = {'q' : '月經'}
        string = ['巧克力', '不理', '黑糖']
        Estring = ['chocolate', 'not care', 'Brown sugar']
        old_img_url = crawler(string, find_param, Estring)
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
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return (text == '巧克力')|(text == '黑糖')|(text == '卡片')|(text == '鞋子')|(text == '手錶')|(text == '禮物')|(text == '道歉')|(text == '親親')
        return False

    def on_enter_happy(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜你度過這次難關")
        self.go_back()

    # for bad end
    def is_going_to_bad(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return (text == '不理')|(text == '放生')
        return False

    def on_enter_bad(self, event):
        sender_id = event['sender']['id']
        btn = [
            {
              "type": "postback",
              "title": "分手吧",
              "payload": "分手吧"
            },
            {
              "type": "postback",
              "title": "不要拜託",
              "payload": "不要拜託"
            },
        ]
        send_text_message(sender_id, "你女友：我們分手吧")
        send_button_message(sender_id, "你想分手嗎？", btn)

    # for breakup
    def is_going_to_breakup(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return (text == '分手吧')
        return False

    def on_enter_breakup(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "水啦恭喜你恢復單身！！")
        self.go_back()

    # for unbreakup
    def is_going_to_unbreakup(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return (text == '不要拜託')
        return False

    def on_enter_unbreakup(self, event):
        sender_id = event['sender']['id']
        btn = [
            {
              "type": "postback",
              "title": "超氣",
              "payload": "超氣"
            }
        ]
        send_text_message(sender_id, "你女友：看在你這麼有誠意的份上，我提示你，我現在正在生氣歐！！")
        send_button_message(sender_id, "她正在生氣嗎？", btn)
    
    # for reangry
    def is_going_to_reangry(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return (text == '超氣')
        return False

    def on_enter_reangry(self, event):
        sender_id = event['sender']['id']
        btn = [
            {
              "type": "postback",
              "title": "親親",
              "payload": "親親"
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
        send_button_message(sender_id, "你女友：給我好好選歐", btn)
