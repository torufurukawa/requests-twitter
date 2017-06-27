from unittest import TestCase, main, mock
import requests_twitter as twitter


class TestRquestsTwitter(TestCase):
    def setUp(self):
        self._auth = twitter.Auth("www", "xxx", "yyy", "zzz")
        self._params = {"q": "foo"}

    @mock.patch.object(twitter.Session, "request")
    def testSessionGet(self, mock_request):
        with twitter.Session(self._auth) as sess:
            resp = sess.get("path", params=self._params)

        self.assertEqual(mock_request.call_count, 1)
        self.assertEqual(mock_request.call_args,
                         (("GET", "path"),
                          {"allow_redirects": True, "params": self._params}))


    @mock.patch.object(twitter.requests.Session, "request")
    def testRequestsRequest(self, mock_request):
        with twitter.Session(self._auth) as sess:
            resp = sess.get("/path", params=self._params)

        self.assertEqual(mock_request.call_count, 1)
        self.assertEqual(mock_request.call_args,
                         (("GET", sess._server + "/path"),
                          {"allow_redirects": True, "params": self._params, "auth": self._auth}))


if __name__ == '__main__':
    main()
