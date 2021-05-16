from flask import Flask, render_template, request, redirect
from dtmf import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    output=''
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        output=display(file)
    return render_template('index.html', out=output)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
