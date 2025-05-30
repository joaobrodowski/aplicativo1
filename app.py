from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user
USER = {"username": "admin", "password": "1234"}

# Dummy hotel data
hotels = [
    {"name": "Hotel Sol", "location": "Rio de Janeiro", "price": "R$250"},
    {"name": "Hotel Praia Azul", "location": "Florianópolis", "price": "R$300"},
    {"name": "Hotel Central", "location": "São Paulo", "price": "R$220"}
]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']
    if username == USER["username"] and password == USER["password"]:
        return redirect(url_for('show_hotels'))
    return "Usuário ou senha inválidos!", 401

@app.route('/hotels')
def show_hotels():
    return render_template('hotels.html', hotels=hotels)

if __name__ == '__main__':
    app.run(debug=True)
