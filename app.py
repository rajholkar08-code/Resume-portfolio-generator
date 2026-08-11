from flask import Flask, render_template, request, send_file
import os
import subprocess
import sys

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# =========================================
# HOME PAGE
# =========================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================
# UPLOAD RESUME
# =========================================

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("resume")

    theme = request.form.get("theme", "blue")

    photo = request.files.get("photo")


    # Check resume

    if not file or file.filename == "":
        return "Please select a resume."


    # Save profile photo

    if photo and photo.filename != "":

        photo.save(
            "static/profile.jpg"
        )


    # Save resume

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "resume.txt"
    )

    file.save(filepath)


    # Run AI portfolio generator

    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )


    # Show errors if main.py fails

    if result.returncode != 0:

        print(result.stdout)

        print(result.stderr)

        return (
            "<h2>Portfolio generation failed.</h2>"
            "<pre>"
            + result.stderr
            + "</pre>"
        )


    # Open generated portfolio

    return render_template(
        "portfolio.html",
        theme=theme
    )


# =========================================
# DOWNLOAD PDF
# =========================================

@app.route("/download")
def download():

    pdf_path = "portfolio.pdf"

    if os.path.exists(pdf_path):

        return send_file(
            pdf_path,
            as_attachment=True
        )

    return "PDF not generated yet."


# =========================================
# RUN FLASK
# =========================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)