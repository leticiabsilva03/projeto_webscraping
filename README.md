# Projeto WebScraping Goodreads

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Repositório: https://github.com/leticiabsilva03/projeto_webscraping

> **Observação**: este projeto foi inicialmente pensado para Letterboxd, mas foi adaptado para coletar dados da estante “read” no Goodreads.

---

## 📋 Descrição

Um scraper em Python que percorre todas as páginas da estante “read” de um usuário no Goodreads, extraindo:

- Título do livro
- Autor
- Nota atribuída pelo usuário
- Ano de publicação
- Avaliação média geral (Goodreads)
- Total de ratings

Os resultados são exportados para um arquivo CSV (`goodreads_read.csv`).

---

## 🚀 Funcionalidades

- Paginação automática pelas páginas de reviews
- Respeito a delays (uso de `time.sleep`) para evitar bloqueios
- Parsers robustos com `requests` e `BeautifulSoup`
- Exportação final para CSV

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/leticiabsilva03/projeto_webscraping.git
   cd projeto_webscraping
   ```

2. (Opcional) crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```

3. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

> **requirements.txt** deve conter:
> ```text
> requests
> beautifulsoup4
> ```


---

## 🛠️ Uso

1. Abra e configure o arquivo `scraper.py` (ou seu script principal):
   ```python
   base_url = 'https://www.goodreads.com/review/list/77564731-leticia'
   shelf = 'read'
   per_page = 100  # itens por página (ajustável)
   ```

2. Execute o scraper:
   ```bash
   python scraper.py
   ```

3. Após execução, confira o CSV gerado:
   ```text
   goodreads_read.csv
   ```

---

## 📁 Estrutura do Projeto

```text
project/
├── src/               # Código-fonte
├── data/              # Dados coletados
├── config/            # Arquivos de configuração
├── Dockerfile         # Configuração do Docker
└── requirements.txt   # Dependências Python
```

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🤝 Contribuição

Pull requests são bem-vindos! Para grandes mudanças, abra primeiro uma issue descrevendo o que deseja alterar.

1. Fork este repositório
2. Crie sua feature branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: descrição da mudança'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---