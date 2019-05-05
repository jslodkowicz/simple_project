from weather import app
from flask import request, jsonify, render_template
from weather.url_requests import *
from weather.measurements import *
from weather.func import *


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route('/json')
def json_page():
    return jsonify({"message": "what's your weather now?"})


@app.route('/result', methods=['POST'])
def get_id():
    city = request.form['textbox']
    return city_temp(city)
    # return render_template("result.html")
