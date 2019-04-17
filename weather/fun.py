from weather import app
from flask import request, jsonify

@app.route('/')
def home():
    return '''
    <form method="POST" action="/result">
        <textarea name="textbox"></textarea>
        <button type="submit" name="submit">Submit</button>
    </form>
    '''

@app.route('/json')
def json_page():
    return jsonify({"message": "what's your weather?"})

@app.route('/result', methods=['POST'])
def get_id():
    id = request.form['textbox']
    return f'Input: {id}'
