"""Twitter plugin for requests"""
import requests
from requests_oauthlib import OAuth1

__version__ = "0.1.0"
_DEFAULT_SERVER = "https://api.twitter.com"



class Auth(OAuth1):
    """Authentication"""

    def __init__(self, consumer_key=None, consumer_secret=None,
                 access_token_key=None, access_token_secret=None):
        """Constructor"""
        super().__init__(consumer_key, consumer_secret,
                         access_token_key, access_token_secret)


class Session(requests.Session):
    """Session"""
    def __init__(self, auth=None, server=None):
        super().__init__()
        self._auth = auth
        self._server = _DEFAULT_SERVER
        if server:
            self._server = server

    def request(self, method, path, **kw):
        """Initiate HTTP request"""
        url = self._server + path
        return super().request(method, url, auth=self._auth, **kw)
