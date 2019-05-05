from weather import app
from flask import request, jsonify, render_template
from weather.url_requests import *
from weather.measurements import *
from weather.func import *
import datetime


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route('/json')
def json_page():
    return jsonify({"message": "what's your weather now?"})


@app.route('/result', methods=['POST'])
def new_fun():
    city = request.form['textbox']
    return get_id(city)

@app.route('/<string:name>')
def get_id(name):
    return render_template("result.html", temp=city_temp(name), name=name.capitalize())
