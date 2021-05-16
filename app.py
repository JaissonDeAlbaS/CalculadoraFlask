# Importamos Flask y paquetes extra
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('app.html')

@app.route("/calculate", methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operacion = request.form['operation']
    
    if num1 == "" or num2 == "":
       return render_template('app.html', result='Operacion erronea, existen campos vacios')
    else:
        if operacion == 'sumar':
            result = float(num1) + float(num2)
            return render_template('app.html', result=result)

        elif operacion == 'restar':
            result = float(num1) - float(num2)
            return render_template('app.html', result=result)

        elif operacion == 'multiplicar':
            result = float(num1) * float(num2)
            return render_template('app.html', result=result)

        elif operacion == 'dividir':
            try:
                result = float(num1) / float(num2)
                return render_template('app.html', result=result)
            except:
                return render_template('app.html', result='Operacion erronea, no se puede dividir entre 0')
            