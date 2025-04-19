import sys
import os
from src.scraper import scrape_film_list, scrape_film_details

# Teste direto no console
films, _ = scrape_film_list(1)
print(f"Filmes encontrados na página 1: {len(films)}")

if films:
    details = scrape_film_details(films[0]['url'])
    print("Detalhes do primeiro filme:", details)

# Adiciona o diretório src ao caminho
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.pipeline import run_pipeline

if __name__ == "__main__":
    run_pipeline(max_pages=1)  # Teste com 1 página primeiro