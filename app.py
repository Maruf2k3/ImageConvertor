from flask import Flask, render_template,request, Response,jsonify
from PIL import Image
import uuid

app = Flask(__name__)
#all GET routes 
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
#Get routes for images
@app.route("/jpgtopng", methods=["GET"])
def jpg_to_png():
    return render_template("jpgtopng.html")

@app.route("/pngtojpg", methods=["GET"])
def png_to_jpg():
    return render_template("pngtojpg.html")

@app.route("/jpgtopdf", methods=["GET"])
def jpg_to_pdf():
    return render_template("jpgtopdf.html")

#Get routes for document

#all Post routes

#JPG to PNG
@app.route("/api/jpgtopng", methods=["POST"])
def jpgtopng_api():
    image = request.files["image"]
    image = Image.open(image)
    image = image.convert("RGBA")

    filename = f"converted_image_{str(uuid.uuid4())}.png"
    image.save(filename, "PNG")

    with open(filename, "rb") as f:
        response = Response(f.read(), content_type="image/png")
        response.headers.set("Content-Disposition", f"attachment; filename={filename}")

    return response

#PNG to JPG
@app.route("/api/pngtojpg", methods=["POST"])
def pngtojpg_api():
    image = request.files["image"]
    image = Image.open(image)
    image = image.convert("RGB")

    filename = f"converted_image_{str(uuid.uuid4())}.jpg"
    image.save(filename, "JPEG")

    with open(filename, "rb") as f:
        response = Response(f.read(), content_type="image/jpeg")
        response.headers.set("Content-Disposition", f"attachment; filename={filename}")

    return response
#Jpg to Pdf
@app.route("/api/jpgtopdf", methods=["POST"])
def jpgtopdf_api():
    image = request.files["image"]
    image = Image.open(image)

    filename = f"converted_image_{str(uuid.uuid4())}.pdf"
    image.save(filename, "PDF")

    with open(filename, "rb") as f:
        response = Response(f.read(), content_type="application/pdf")
        response.headers.set("Content-Disposition", f"attachment; filename={filename}")

    return response



if __name__ == "__main__":
    app.run(debug=True)
