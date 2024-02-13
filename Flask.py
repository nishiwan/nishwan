from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/my/secret/page")
def secret():
    return "SHHH"

@app.route("/usr/<username>")
def user_page(username):
    return f"Welcome, {username}"

@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page for the post # {post_id}"

@app.route("/parellsenar/<int:numero>")
def parellsenar(numero):
    if numero % 2 == 0:
        return f"el numero {numero} es parell"
    else:
        return f"el numero {numero} es impar"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/<nombre>/<int:edad>")
def calcular_cumpleanos(nombre, edad):
    año_actual = datetime.datetime.now().year
    años_faltantes = 100 - edad
    año_cumpleaños = año_actual + años_faltantes

    mensaje = f"Hola {nombre}, cumplirás 100 años en el año {año_cumpleaños}."
    
    return render_template('hello.html', mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
