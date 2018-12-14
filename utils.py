import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAIDkh81WEwBAO1yFsbgIeulOS42VQ3QDyZAqIUye4sYkcZCNXbcC69z0OQ4f7zjLALQODDrxbcTnbjYXtlpIrPGh7au6VOM4FKxFygCD7iYWVTpW1w3LJ7hAQZCkqqJS3lZAueyGkOZB55ZApZBBd6SpD4Hv0apRa7n15Kg2UjdAZDZD"


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
