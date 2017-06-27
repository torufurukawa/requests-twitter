# requests-twitter
Twitter support for Python Requests

## Requirements

- Python 3.5 or later

## Example

```
import requests_twitter as twitter

CONSUMER_KEY = "..."
CONSUMER_SECRET = "..."
ACCESS_TOKEN_KEY = "..."
ACCESS_TOKEN_SECRET = "..."

auth = twitter.Auth(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
sess = twitter.Session(auth)
resp = sess.get("/1.1/search/tweets.json", params={"q": u"hello"})

print(resp.status_code)
print(resp.json())
```


## Install

To setup environment, run the folling commands.

```
pip install -r requirements.txt
```

To test, run the following command.

```
python tests.py
```

