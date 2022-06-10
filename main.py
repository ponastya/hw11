from utils import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    candidates = load_candidates()
    return render_template("list.html", candidate=candidates)

app.run()