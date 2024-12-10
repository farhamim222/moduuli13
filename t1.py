from flask import Flask, jsonify

app = Flask(__name__)

def num(luku):
    if luku <= 1:
        return False
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return True

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/alkuluku/<number>')
def tarkistus(number):
    try:
        number = int(number)
        vastaus = {
            "Number": number,
            "IsPrime": num(number),
        }
        return jsonify(vastaus)
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter a valid integer."})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
