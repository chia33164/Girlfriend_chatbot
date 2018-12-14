import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAIDkh81WEwBAOiGTIapComwtt4Jv59B8m1wsUXyuKFAUDnO2jQP9LcGb2LLWNCUm11j4kC98L1KgXdK8n1hqUR4GmpusoTsT0WET67ZAKqzqEdo7VdjgISRZAOeKZAY2lE5Tg8p5fOPMc3KeH2l1AE5kfkTlLWH4GIReoOlwZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
