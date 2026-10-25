from flask import Flask, render_template, request, send_from_directory
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():

    room = "main"

    images = []

    if os.path.exists(UPLOAD_FOLDER):
        images = os.listdir(UPLOAD_FOLDER)
        images.reverse()

    return render_template(
        "pc.html",
        room=room,
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

        filename = str(uuid.uuid4()) + "_" + file.filename

        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(filepath)

        return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>✅送信完了！</h1>
</body>
</html>
"""

    return render_template("mobile.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        UPLOAD_FOLDER,
        filename
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    