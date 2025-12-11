from flask import Flask, render_template, request
from extraer import extraer_titulo
from apichecker import consultar_apigugul
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userform_input = request.form['input_userform']
        api_key=os.getenv('google_API')
        if userform_input.startswith('https'):
            termino_busqueda = extraer_titulo(userform_input)
        else:
            termino_busqueda = userform_input

        results_dict = consultar_apigugul(termino_busqueda, api_key)
    elif request.method== 'GET':
        results_dict = None
    return render_template ('index.html', resultados=results_dict)
if __name__ == '__main__':
    app.run(debug=True)