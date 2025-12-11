#Mis importaciones :)
import requests, os
from pathlib import Path
from bs4 import BeautifulSoup
import json
from extraer import extraer_titulo
from apichecker import consultar_apigugul
from colorama import init, Fore, Style

init(autoreset=True, wrap=True)
api_key=os.getenv('google_API')

print('¿Bienvenido a Fast-Checker. \n ¿Que deseas verificar?')
user_input = input()
if user_input.startswith('https'):
    termino_busqueda = extraer_titulo(user_input)
else:
    termino_busqueda = user_input

claims = consultar_apigugul(termino_busqueda, api_key)


if claims:
        for claim in claims:
            texto = claim['text']
            autor = claim['claimReview'][0]['publisher']['name']
            titulo = claim['claimReview'][0]['title']
            rating = claim['claimReview'][0]['textualRating']
            color_rating = rating.lower()
            print(f'{texto}')
            print(f'Autor {autor}')
            print(f'Título: {titulo}')
            if 'fals' in color_rating or 'fak' in color_rating:
                print('Conclusión: ' + Fore.RED + f'{rating}')
                print('---------------------------------')
            elif 'verdader' in color_rating or 'true' in color_rating:
                     print(f'Conclusión: ' + Fore.GREEN + f'{rating}')
                     print('---------------------------------')
            else:
                print(f'Conclusión: ' + Fore.YELLOW + f'{rating}')
                print('---------------------------------')
                  
else:
        print('Lo siento, no se encontraron verificaciones oficiales sobre este tema.')












    