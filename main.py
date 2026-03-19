from flask import Flask
app = Flask(__name__)

@app.route('/exam/')
def index():
    return 'Bienvenue, Jusline Florial!'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')