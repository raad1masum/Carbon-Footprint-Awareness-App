import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

from api import guessIMG

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index_pg():
    return render_template("index.html")


@app.route('/about')
def about_pg():
    return render_template("about.html")


@app.route('/tracker')
def tracker_pg():
    return render_template("tracker.html")


@app.route('/scanner')
def scanner_pg():
    return render_template("scanner.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/scanner', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'error'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'error'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            guess = guessIMG(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return guess
        else:
            return 'error'


if __name__ == "__main__":
    app.run("127.0.0.1", port=3000, debug=True)
