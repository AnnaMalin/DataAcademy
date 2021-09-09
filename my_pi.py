from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify('Hello, World!')


@app.route('/user')
def get_users():
    users = [
        {"id": 1, "name": "Sebastian","country": "se"},
        {"id": 2,"name": "Pekka","country": "fi"},
        {"id": 3,"name": "John","country": "us"}
    ]
    return jsonify(users=users)




if __name__ == '__main__':
    app.run()