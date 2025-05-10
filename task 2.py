from flask import Flask, render_template, request
import requests

app = Flask(__name__)  # corrected __name__

UNSPLASH_ACCESS_KEY = "2fARolRwOMyLEt5ekCsBRfYYGgetZ1WpWNWs6Sjl8Rs"

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        width = request.form.get("width")
        height = request.form.get("height")
        if width and height:
            response = requests.get(
                "https://api.unsplash.com/photos/random",
                headers={"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
            )
            data = response.json()
            raw_image_url = data["urls"]["regular"]
            # Append width & height as query params (optional)
            image_url = f"{raw_image_url}&w={width}&h={height}"
    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":  # corrected __name__
    app.run(debug=True)
