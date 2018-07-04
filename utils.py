import re
from subprocess import check_output
import hashlib


def letterify(image_path):
    """extract letters from an image using tesseract, return a list
    of letters

    :param image_path: str

    """
    # use tesseract executable and get result from
    # standard output
    command = ['tesseract', image_path, 'stdout']
    output = check_output(command)
    # the result above is bytes, need to decode to str
    output = output.decode('utf-8')
    # using regular expressing to find all letters
    letters = re.findall(r'\w', output)
    return letters


def get_md5(fname):
    """get md5 checksum of a file
    adopt from https://stackoverflow.com/a/3431838
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def is_image_file(filename):
    """check filename suffix, if it's an image"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png']
