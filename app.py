import os
from flask import Flask, request, jsonify, url_for, abort
from flask_redis import FlaskRedis
from werkzeug.utils import secure_filename
import json
from utils import get_md5, letterify, is_image_file


CURRENT_DIR = os.path.dirname(__name__)
UPLOAD_FOLDER = os.path.join(CURRENT_DIR, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    try:
        os.makedirs(UPLOAD_FOLDER)
    except Exception:
        pass
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REDIS_URL'] = "redis://db:6379/0"
redis_store = FlaskRedis(app)


def save_to_db(md5, letters, query_url):
    """save results to database
    :param md5, str
    :param letters, list
    :query url, str
    """
    query_url = 'http://' + request.host + query_url
    data = {"key": md5, 'letters': letters, "query_url": query_url}
    redis_store.set(md5, json.dumps(data))
    return data


def query_db(md5):
    """get result from database, using md5 as query key
    return result if key exists, otherwise return an
    empty dict
    :param md5, str
    """
    res = redis_store.get(md5)
    if res:
        return json.loads(res)
    return {}


@app.route('/', methods=['GET', 'POST'])
def index():
    """adopt from flask documentation,
    a request handler to process image uploads
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'no file', 400
        file = request.files['file']
        # file is an image file with png,jpg suffix
        if file and is_image_file(file.filename):
            # avoid malicious filename
            filename = secure_filename(file.filename)
            # get file path on system
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # save file to disk
            file.save(upload_path)
            # get md5 of file
            md5 = get_md5(upload_path)
            # check if image exists
            res = query_db(md5)
            if res:
                return jsonify(res)
            # otherwise extract letters from image
            try:
                letters = letterify(upload_path)
            except Exception as e:
                app.logger.error(e)
                abort(400)
            # build query url
            query_url = url_for('result', key=md5)
            # save result to db
            data = save_to_db(md5, letters, query_url)
            return jsonify(data)
        else:
            return 'file type not supported', 400

    return "Letterify is service to extract letters from images."


@app.route("/<key>", methods=["GET"])
def result(key):
    res = query_db(key)
    return jsonify(res), 200 if res else 404


if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)
