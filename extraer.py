import requests
from bs4 import BeautifulSoup

#headersows
headers_falsos = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    
    'Referer': 'https://www.google.com/',
    
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}
def extraer_titulo(url):
    response = requests.get(
        url,
        headers=headers_falsos
    )
    response_text = response.text
    sopa = BeautifulSoup(response_text, 'html.parser')
    titulo_raw = sopa.title.string
    titulo = titulo_raw.strip()
    return titulo
