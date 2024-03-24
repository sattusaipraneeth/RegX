# app.py
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        test_string = request.form["test_string"]
        regex_pattern = request.form["regex_pattern"]
        matches = re.findall(regex_pattern, test_string)
        return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)
    return render_template("index.html")

@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return jsonify(result="Valid Email Address")
    else:
        return jsonify(result="Invalid Email Address")

if __name__ == '__main__':
    app.run(debug=True)


