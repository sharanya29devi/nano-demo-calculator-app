from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if num_1 in data and num_2 in data:
        return num_1 + num_2
    else: 
        return jsonify({'error': 'Please provide num1 and num2 in JSON format.'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if num_1 in data and num_2 in data:
        return num_1 - num_2
    else: 
        return jsonify({'error': 'Please provide num1 and num2 in JSON format.'}), 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
