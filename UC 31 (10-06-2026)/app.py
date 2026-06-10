from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def inicio():

    nome = request.cookies.get('nome')

    tema = request.cookies.get('tema')

    if tema == None:
        tema = 'claro'

    return render_template('inicio.html', nome=nome, tema=tema)

@app.route('/salvar', methods=['POST'])
def salvar():

    nome = request.form.get('nome')

    resposta = make_response(render_template('inicio.html', nome=nome, tema='claro'))

    resposta.set_cookie('nome', nome)

    return resposta

@app.route('/tema/<modo>')
def tema(modo):

    nome = request.cookies.get('nome')

    resposta = make_response(render_template('inicio.html', nome=nome, tema=modo))

    resposta.set_cookie('tema', modo)

    return resposta

if __name__ == '__main__':
    app.run(debug=True)