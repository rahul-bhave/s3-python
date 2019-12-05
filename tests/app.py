import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from s3_demo import upload_file
from s3_demo import list_files
from s3_demo import download_file

app = Flask(__name__,template_folder='../templates')
UPLOAD_FOLDER = "uploads"
BUCKET = "rahulb-test-bucket"


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    contents = list_files("rahulb-test-bucket")
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)

        return redirect("/storage")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6868)