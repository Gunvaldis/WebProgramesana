from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Audi')
def Audi():
    return render_template('audi.html')

@app.route('/BMW')
def BMW():
    return render_template('BMW.html')

@app.route('/Mercedes')
def Mercedes():
    return render_template('Mercedes.html')

@app.route('/Loterija')
def Loterija():
    return render_template('Loterija.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)