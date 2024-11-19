from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 

        # Procesar los datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        # Aquí puedes hacer algo con los datos, como guardarlos en una base de datos
        return 'Gracias, ' + nombre + '! Tu email es: ' + email
    else:
        return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)