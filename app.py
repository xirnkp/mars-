from flask import Flask, render_template, request, jsonify
from dbtest import save_data_to_database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    name = request.form['name_give']
    address = request.form['address_give']
    size = request.form['size_give']

    data = {
        'name': name,
        'address': address,
        'acres': size
    }
    
    save_data_to_database(data)
    return jsonify({'msg': 'POST request!'})

@app.route("/mars", methods=["GET"])
def mars_get():
    return jsonify({'msg': 'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
