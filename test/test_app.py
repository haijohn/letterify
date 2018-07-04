import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['REDIS_URL'] = "redis://db:6379/1"
        self.app = app
        self.client = app.test_client()

    def test_upload_file(self):
        fpath = 'test/test_data/images.png'
        fname = 'images.png'
        res = self.client.post('/', data={
            'file': (open(fpath, 'rb'), fname)
        })
        assert res.status_code == 200
        assert ''.join(res.json['letters']) == 'images'

    def test_empty_upload(self):
        res = self.client.post('/', data={})
        assert res.status_code == 400

    def test_txt_upload(self):
        fpath = 'test/test_data/test.txt'
        fname = 'test.txt'
        res = self.client.post('/', data={
            'file': (open(fpath, 'rb'), fname)
        })
        assert res.status_code == 400

    def test_upload_file_and_query(self):
        fpath = 'test/test_data/images.png'
        fname = 'images.png'
        res = self.client.post('/', data={
            'file': (open(fpath, 'rb'), fname)
        })
        key = res.json['key']
        request_res = self.client.get('/' + key)
        assert request_res.json['key'] == key

    def tearDown(self):
        """remove data after test"""
        self.app.extensions['redis'].flushall()
