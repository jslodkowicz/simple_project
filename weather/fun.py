from weather import app
from flask import request, jsonify, render_template


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route('/json')
def json_page():
    return jsonify({"message": "what's your weather now?"})


@app.route('/result', methods=['POST'])
def get_id():
    id = request.form['textbox'] # noqa
    return render_template("result.html")
