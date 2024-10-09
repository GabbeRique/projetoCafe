from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#armazenar os cafés
cafes = []

# Rota raiz: Exibe a página principal com a lista de cafés
@app.route('/')
def index():
    return render_template('index.html', cafes=cafes)

# Rota para criar um novo café
@app.route('/criar', methods=['POST'])
def create():
    nome = request.form['nome']
    cafes.append(nome)
    return redirect('/')

# Rota para alterar o nome de um café
@app.route('/alterar', methods=['POST'])
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    if old_name in cafes:
        index = cafes.index(old_name)
        cafes[index] = new_name
    return redirect('/')

# Rota para apagar um café
@app.route('/apagar', methods=['POST'])
def delete():
    nome = request.form['nome']
    if nome in cafes:
        cafes.remove(nome)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
