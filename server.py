import os
from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "KeepItSecretKeepItSafe"
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def select_file():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        flash("Your file upload failed. Please try again.", "red")
    file = request.files['file']
    if file.filename == '':
        flash("Your file upload failed. Please try again.", "red")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("Your file has been successfully uploaded!", "green")
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html")
app.run(debug=True)