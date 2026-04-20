from flask import Flask, render_template
from core.db import load_entries

app = Flask(__name__)

@app.route("/")
def index():
    data = load_entries()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
