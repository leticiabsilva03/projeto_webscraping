# Web scraping da estante “read” no Goodreads com paginação
# Requer pacotes: requests, beautifulsoup4
# Instale com: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import time
import re
import csv
import os

# Configura sessão com headers
session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    )
})

# Função para extrair dados de página de livro
def parse_book_page(book_url):
    pub_year = avg_rating = rating_count = None
    try:
        resp = session.get(book_url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        # Ano de publicação
        m = re.search(r'First published.*?(\d{4})', text, re.I) or \
            re.search(r'Published.*?(\d{4})', text, re.I)
        if m:
            pub_year = m.group(1)
        # Avaliação média e contagem
        m2 = re.search(r'(\d+\.\d+)\s+([0-9,]+)\s+ratings?', text)
        if m2:
            avg_rating = float(m2.group(1))
            rating_count = int(m2.group(2).replace(',', ''))
        time.sleep(1)
    except Exception:
        pass
    return pub_year, avg_rating, rating_count

# Itera sobre as páginas da estante
base_url = (
    'https://www.goodreads.com/review/list/77564731-leticia'
)
shelf = 'read'
per_page = 100   # máximo por página (ajusta se suportar)
page = 1
books = []
rating_map = {
    'did not like it': 1,
    'it was ok': 2,
    'liked it': 3,
    'really liked it': 4,
    'it was amazing': 5
}

while True:
    params = {
        'shelf': shelf,
        'per_page': per_page,
        'page': page
    }
    resp = session.get(base_url, params=params)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.find_all('tr', id=lambda x: x and x.startswith('review_'))
    if not rows:
        break
    print(f"Página {page}: {len(rows)} livros encontrados")
    for row in rows:
        # Título e URL
        a = row.select_one('td.field.title a.bookTitle') or row.select_one('td.field.title a')
        if not a:
            continue
        title = a.get_text(strip=True)
        href = a['href'].split('?')[0]
        book_url = 'https://www.goodreads.com' + href
        # Autor
        author = (row.select_one('td.field.author a') or {}).get_text(strip=True)
        # Nota da usuária
        star = row.select_one('td.field.rating span.staticStars')
        if star and star.has_attr('title'):
            user_rating = rating_map.get(star['title'].lower(), None)
        else:
            sel = row.select_one('td.field.rating option[selected]')
            user_rating = int(sel['value']) if sel and sel.has_attr('value') else None
        # Detalhes extras
        pub_year, avg_rating, rating_count = parse_book_page(book_url)
        books.append({
            'title': title,
            'author': author,
            'user_rating': user_rating,
            'published_year': pub_year,
            'avg_rating': avg_rating,
            'ratings_count': rating_count
        })
    page += 1
    time.sleep(1)

print(f"Total de livros coletados: {len(books)}")
# Exporta para CSV
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

output_path = os.path.join(DATA_DIR, 'goodreads_read.csv')

with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title','author','user_rating','published_year','avg_rating','ratings_count'])
    writer.writeheader()
    writer.writerows(books)

print("CSV salvo como 'goodreads_read.csv'")