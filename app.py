from flask import Flask, request, jsonify
from flask_cors import CORS
from extraer import extraer_titulo
from checker import consultar_apigugul
from scraping_chile import scrapear_fuentes_chilenas, busqueda_general
import os

app = Flask(__name__)

# PARCHE: Configuración robusta de CORS para SvelteKit
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/api/verify', methods=['POST'])
def verify():
    try:
        data = request.json
        user_input = data.get('query', '')
        # Asegúrate de tener esta variable de entorno cargada
        api_key = os.getenv('google_API')

        # Procesamiento de URL o texto
        termino = extraer_titulo(user_input) if user_input.startswith('https') else user_input
        
        # Ejecución de fuentes en paralelo (secuencial en este caso)
        res_google = consultar_apigugul(termino, api_key) or []
        res_chile = scrapear_fuentes_chilenas(termino) or []
        
        # Parche para búsqueda web sin "?"
        query_web = termino if "?" in termino else f"{termino} noticias chile"
        res_web = busqueda_general(query_web) or []

        return jsonify({
            "success": True,
            "termino": termino,
            "results": {
                "google": res_google,
                "chile": res_chile,
                "web": res_web
            }
        })
    except Exception as e:
        print(f"Error en servidor: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    # PARCHE: Host 0.0.0.0 para evitar problemas de resolución en Fedora/Linux
    app.run(debug=True, port=5000, host='0.0.0.0')