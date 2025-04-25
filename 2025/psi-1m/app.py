from flask import Flask, render_template, \
request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/register", methods=['GET']) #'GET', 
# def cadastro():
#     nome = request.form['nome']
#     return f"Você digitou <b>{nome}</b>"

# @app.route("/register", methods=['POST']) #'GET', 
# def cadastro():
#     nome = request.form['nome']
#     return f"Você digitou <b>{nome}</b>"

# @app.route("/register", methods=['GET', 'POST'])
# def cadastro():
#     if request.method == 'POST':
#         nome = request.form['Alguém']
#         return f"Você digitou {nome}"
#     else:
#         return render_template('index.html')

@app.route('/cores', methods=['POST'])
def cores():
    cor = ""
    if 'cor' in request.args.values():
        cor = request.args.get('cor')
        print(cor)
    return render_template('cookies.html', cor=cor)