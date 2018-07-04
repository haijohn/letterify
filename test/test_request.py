import requests
import unittest


class RequestTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_request(self):
        url = 'http://localhost:5000'
        filepath = 'test/test_data/1.png'
        with open(filepath, 'rb') as f:
            files = {'file': f}
            r = requests.post(url, files=files)
        assert r.status_code == 200
