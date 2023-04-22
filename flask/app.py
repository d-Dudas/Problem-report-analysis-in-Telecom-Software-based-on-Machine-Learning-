from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from the Flask API!', 'msg': 'Ana are mere!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
