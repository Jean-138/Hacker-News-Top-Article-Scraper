

Este projeto em Python realiza web scraping no site Hacker News para identificar o artigo com maior número de votos na página principal.

O programa faz uma requisição HTTP para a página de notícias, analisa o HTML retornado, extrai os títulos, links e votos dos artigos e identifica qual deles possui mais upvotes. Ao final, exibe no terminal o título e o link do artigo mais votado.

***

## Tecnologias Utilizadas

- Python  
- requests  
- beautifulsoup4  

***

## Estrutura do Projeto

- `main.py`  
- `requirements.txt`  

***

## Como Funciona

- O programa envia uma requisição GET para a página principal do Hacker News.  
- O HTML retornado é armazenado em uma variável.  
- O BeautifulSoup interpreta o HTML.  
- O código coleta todos os títulos e links dos artigos.  
- O código coleta todos os votos dos artigos.  
- Os votos são convertidos para números inteiros.  
- O programa identifica o maior número de votos.  
- O título e o link correspondentes são exibidos no terminal.  

***

## Como Executar

Clone o repositório:

```
git clone https://github.com/Jean-138/Hacker-News-Top-Article-Scraper.git
```

Entre na pasta do projeto:

```
cd Hacker-News-Top-Article-Scraper
```

Instale as dependências:

```
pip install -r requirements.txt
```

Execute o arquivo:

```
python main.py
```

***

## Objetivo

Praticar requisições HTTP, análise de HTML com BeautifulSoup, manipulação de listas e lógica para encontrar o maior valor dentro de uma coleção de dados.
