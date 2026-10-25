from flask import Flask, render_template, request, send_from_directory
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():

    images = []

    if os.path.exists(UPLOAD_FOLDER):
        images = os.listdir(UPLOAD_FOLDER)
        images.reverse()

    room_id = "main"

    return render_template(
        "pc.html",
        room=room_id,
        images=images
    )


@app.route("/upload/<room>", methods=["GET", "POST"])
def upload(room):

    if request.method == "POST":

        if "image" not in request.files:
            return "画像が選択されていません"

        file = request.files["image"]

        if file.filename == "":
            return "画像が選択されていません"

        filename = 
str(uuid.uuid4()) + os.path.splitext(file.filename)[1]

        file.save(os.path.join(UPLOAD_FOLDER, filename))

        return "画像がアップロードされました"

    return render_template("upload.html", room=room) 