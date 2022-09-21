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



@app.route('/forma', methods = ['GET', 'POST'])
def forma():
    if request.method == 'GET':
        return render_template('forma.html')

    elif request.method == 'POST':
        firstname = request.form.get('first-name')
        lastname = request.form.get('last-name')
        email = request.form.get('email')
        password = request.form.get('new-password')

        dataline = f"{firstname},{lastname},{email},{password}\n"

        with open("users.csv", "a", encoding="utf-8") as f:
            f.write(dataline)

        return render_template('forma.html', message = "Paldies, jūsu atbilde pieņemta!")

    else:   
        return "ERROR"


if __name__ == '__main__':
    app.run(debug=True, port=8080)