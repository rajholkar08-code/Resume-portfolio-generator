from flask import Flask, render_template, request
import os
from flask import send_file
import pdfkit

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    # Save Resume
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "resume.txt"
    )

    file.save(filepath)

    # Save Photo (optional)
    photo = request.files.get("photo")

    if photo and photo.filename != "":
        os.makedirs("static", exist_ok=True)
        photo.save("static/profile.jpg")

    # Run Generator
    os.system("python main.py")

    # Show Portfolio
    return render_template("portfolio.html")

@app.route("/download")
def download_pdf():

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    )

    pdfkit.from_file(
        "templates/portfolio.html",
        "portfolio.pdf",
        configuration=config
    )

    return send_file(
        "portfolio.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)