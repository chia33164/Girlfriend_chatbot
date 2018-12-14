# TOC-Bot-Demo-2019

A Basic Messenger Echo Bot Based on python & bottle framework.

## Setup

### Prerequisite
* Python 3
* Facebook Page and App
* HTTPS Server (Heroku)

#### Install Dependency
```sh
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

#### Secret Data

- Setup environment variables ```VERIFY_TOKEN```, ```ACCESS_TOKEN```, ```PORT```

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python app.py
```
