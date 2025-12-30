# checker.py
import requests, os
from colorama import init, Fore
# Mantén tus otros imports...

init(autoreset=True)

def consultar_apigugul(query, api_key, locale='es-CL'):
    # Añadimos languageCode a la URL para filtrar resultados
    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={query}&key={api_key}&languageCode={locale}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data.get('claims', [])
    except Exception as e:
        print(f"Error API Google: {e}")
        return []

# --- ESTO ES LO QUE ARREGLA TU PROBLEMA ---
if __name__ == '__main__':
    # Todo lo que esté AQUÍ ADENTRO solo se ejecutará si corres el archivo directamente
    # Pero Flask lo ignorará cuando lo importe.
    api_key = os.getenv('google_API')
    print('Bienvenido a CheckMate (Modo Consola)')
    user_input = input('¿Qué deseas verificar? ')
    
    # ... tu lógica actual de prints y colores ...
    results = consultar_apigugul(user_input, api_key)
    if results:
        for claim in results:
            print(f"Resultado: {claim['claimReview'][0]['textualRating']}")
    else:
        print("No se encontraron resultados.")









    