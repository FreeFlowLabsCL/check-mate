import requests, os
from pathlib import Path
import json

def consultar_apigugul(termino_busqueda, clave_api):
    api_key = os.getenv('google_API')
    ruta_respuestas = Path('./respuestas')
    respuestafile = ruta_respuestas/'respuesta.json'
    respuesta = requests.get(
        "https://factchecktools.googleapis.com/v1alpha1/claims:search",
        params={
            'key': api_key,
            'query' :  termino_busqueda,
             'languageCode' : 'es'
        }        
    )
    respuesta_json = respuesta.json()
    if 'claims' in respuesta_json and respuesta_json['claims']:
        print(f'Se encontraron {len(respuesta_json['claims'])} resultados')

        return respuesta_json['claims']
    else:
        return []