from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def pc():
    room_id = str(uuid.uuid4())[:8]
    return render_template("pc.html", room=room_id)

@app.route("/upload/<room>", methods=["GET", "POST"])
def upload(room):

    if request.method == "POST":

        file = request.files["image"]

        filename = str(uuid.uuid4()) + "_" + file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(path)

        return f"""
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="2;url=/upload/{room}">
</head>
<body style="text-align:center;font-size:40px;">
✅送信完了！<br><br>
次の画像を選択できます
</body>
</html>
"""

    return render_template("mobile.html", room=room)

if __name__ == "__main__":
    app.run(debug=True)
    