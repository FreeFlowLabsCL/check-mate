import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def busqueda_general(query):
    resultados_gen = []
    try:
        # Usamos la URL de búsqueda sin filtros de tiempo para asegurar que siempre haya algo
        import urllib.parse
        encoded_query = urllib.parse.quote(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Cambiamos el selector a uno más genérico por si cambian la clase
        links = soup.find_all('a', class_='result__a')
        snippets = soup.find_all('a', class_='result__snippet')

        for i in range(len(links[:5])):
            resultados_gen.append({
                'text': query,
                'claimReview': [{
                    'publisher': {'name': 'Web General'},
                    'title': links[i].get_text(strip=True),
                    'textualRating': snippets[i].get_text(strip=True) if i < len(snippets) else "Ver más en el link",
                    'url': links[i]['href']
                }]
            })
    except Exception as e:
        print(f"Error web: {e}")
    return resultados_gen
def scrapear_fuentes_chilenas(query):
    resultados_cl = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # --- SCRAPING FAST CHECK CL ---
    try:
        url_fc = f"https://www.fastcheck.cl/?s={query.replace(' ', '+')}"
        res = requests.get(url_fc, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        for article in soup.select('article')[:3]:
            title_tag = article.select_one('.entry-title a')
            if title_tag:
                resultados_cl.append({
                    'text': query,
                    'claimReview': [{
                        'publisher': {'name': 'Fast Check CL'},
                        'title': title_tag.get_text(strip=True),
                        'textualRating': 'Verificación de Prensa',
                        'url': title_tag['href']
                    }]
                })
    except Exception as e: print(f"Error FC: {e}")

    # --- SCRAPING FACTCHECK PUC ---
    try:
        url_puc = f"https://factcheck.puc.cl/search?q={query.replace(' ', '+')}"
        res_puc = requests.get(url_puc, headers=headers, timeout=5)
        soup_puc = BeautifulSoup(res_puc.text, 'html.parser')
        for item in soup_puc.select('.search-result-item')[:3]:
            link = item.select_one('a')
            if link:
                resultados_cl.append({
                    'text': query,
                    'claimReview': [{
                        'publisher': {'name': 'FactCheck PUC'},
                        'title': link.get_text(strip=True),
                        'textualRating': 'Análisis Académico',
                        'url': "https://factcheck.puc.cl" + link['href'] if not link['href'].startswith('http') else link['href']
                    }]
                })
    except Exception as e: print(f"Error PUC: {e}")

    return resultados_cl