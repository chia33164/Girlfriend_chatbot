from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_birthday(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'birthday'
        return False

    def is_going_to_angry(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'angry'
        return False

    def on_enter_birthday(self, event):
        print("Her Birthday is comming , what can i do ?")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Her Birthday is comming , what can i do ?")
        self.go_back()

    def on_exit_birthday(self):
        print('Leaving birthday')

    def on_enter_angry(self, event):
        print("She is angry now")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "She is angry now")
        self.go_back()

    def on_exit_angry(self):
        print('Leaving angry')
