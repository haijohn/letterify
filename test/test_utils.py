import unittest
from utils import (letterify, get_md5,
                   is_image_file)


class LetterifyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_english_letter(self):
        image_path = 'test/test_data/images.png'
        rv = letterify(image_path)
        assert rv == ['i', 'm', 'a', 'g', 'e', 's']

    def test_blank(self):
        image_path = 'test/test_data/blank.png'
        rv = letterify(image_path)
        assert rv == []

    def test_chinese(self):
        image_path = 'test/test_data/chinese.png'
        rv = letterify(image_path)
        assert rv == []


class MD5TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_two_same_file_with_different_name(self):
        fpath1 = 'test/test_data/1.png'
        fpath2 = 'test/test_data/2.png'
        assert get_md5(fpath1) == get_md5(fpath2)


class IsImageTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_png(self):
        fname = 'a.png'
        assert is_image_file(fname)

    def test_jpg(self):
        fname = 'a.jpg'
        assert is_image_file(fname)

    def test_txt(self):
        fname = 'txt'
        assert not is_image_file(fname)
