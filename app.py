from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Obrigatório para usar flash()

registered_users = []  # Armazena os usuários cadastrados em memória

@app.route('/')
def index():
    return redirect(url_for('cadastro'))

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    # Validação simples
    if not username or not email or not password:
        flash('Por favor, preencha todos os campos obrigatórios.')
        return redirect(url_for('cadastro'))

    if len(password) < 8:
        flash('A senha deve conter pelo menos 8 caracteres.')
        return redirect(url_for('cadastro'))

    # Armazenar usuário (apenas para demonstração — NÃO armazene senhas em texto puro em produção!)
    user = {
        'username': username,
        'email': email,
        'password': password,
    }
    registered_users.append(user)

    flash('Cadastro realizado com sucesso! Bem-vindo ao site de notícias.')
    return redirect(url_for('servicos'))  # redireciona para /servicos após cadastro

if __name__ == '__main__':
    app.run(debug=True)
