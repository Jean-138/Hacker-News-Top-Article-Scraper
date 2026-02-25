from bs4 import BeautifulSoup  # Importa a biblioteca BeautifulSoup para parsear HTML.
import requests  # Importa a biblioteca requests para realizar requisições HTTP.

# Faz a requisição GET ao site do Hacker News para pegar a página de notícias.
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text  # Guarda o conteúdo HTML da página retornada.

# Usa BeautifulSoup para fazer o parsing do HTML e facilitar a extração de dados.
soup = BeautifulSoup(yc_web_page, "html.parser")

# Pega todos os artigos da página, que estão dentro de <span class="titleline">
all_articles = soup.find_all(name="span", class_="titleline")

# Duas listas para armazenar os textos dos artigos e seus links
article_texts = []
article_links = []

# Para cada artigo encontrado, pega o texto (título) e o link
for article in all_articles:
    anchor = article.find("a")  # Encontra a tag <a> dentro do <span> que contém o título e o link.
    text = anchor.getText()  # Pega o texto (título) do artigo.
    article_texts.append(text)  # Adiciona o texto do artigo à lista.
    link = anchor.get("href")  # Pega o link do artigo.
    article_links.append(link)  # Adiciona o link à lista.

# Cria uma lista com os votos dos artigos, pegando o número dentro de <span class="score">
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# Encontra o maior número de votos (artigo mais popular)
largest_number = max(article_upvotes)  # Pega o maior número de votos.
largest_index = article_upvotes.index(largest_number)  # Encontra o índice do artigo com o maior número de votos.

# Imprime o título e o link do artigo com o maior número de votos
print(article_texts[largest_index])  # Imprime o título do artigo mais votado.
print(article_links[largest_index])  # Imprime o link do artigo mais votado.

# As linhas abaixo estão comentadas, mas mostram como você pode imprimir os títulos, links ou votos.
# print(article_texts)  # Imprime todos os títulos dos artigos.
# print(article_links)  # Imprime todos os links dos artigos.
# print(article_upvotes)  # Imprime todos os números de votos dos artigos.