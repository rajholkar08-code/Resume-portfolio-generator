from flask import Flask, render_template, request, send_file
import os
import subprocess
import sys

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("resume")

    theme = request.form.get("theme", "blue")

    photo = request.files.get("photo")

    if not file or file.filename == "":
        return "Please select a resume."

    # Delete old resumes
    for f in os.listdir(UPLOAD_FOLDER):

        path = os.path.join(
            UPLOAD_FOLDER,
            f
        )

        if os.path.isfile(path):
            os.remove(path)

    # Save profile image
    if photo and photo.filename != "":
        photo.save("static/profile.jpg")

    # Save uploaded resume
    filename = file.filename

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)

    # Run AI Generator
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        return (
            "<h2>Portfolio generation failed.</h2>"
            "<pre>"
            + result.stderr +
            "</pre>"
        )

    return render_template(
        "portfolio.html",
        theme=theme
    )


@app.route("/download")
def download():

    pdf_path = "portfolio.pdf"

    if os.path.exists(pdf_path):

        return send_file(
            pdf_path,
            as_attachment=True
        )

    return "PDF not generated yet."


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )