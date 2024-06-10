# Dependências: rich, feedparser.

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.padding import Padding
import feedparser
import os

# Função para limpar o console dependendo do sistema operacional!
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# URL do feed RSS TabNews!
feed_url = "https://www.tabnews.com.br/recentes/rss"

feed = feedparser.parse(feed_url)

# Ordena os itens do feed pelo tempo de publicação (do mais recente para o mais antigo).
sorted_entries = sorted(feed.entries, key=lambda x: x.published_parsed, reverse=True)

console = Console()

# Tabela Feed RSS.
table = Table(title="TabNews", show_header=True, header_style="bold magenta")
table.add_column("Nº", style="cyan", justify="right")
table.add_column("Título", style="cyan")
table.add_column("Descrição e Link", style="green")

# Dicionário para mapear os títulos aos links.
title_to_link = {}

# Itens do feed à tabela e ao dicionário de mapeamento.
for index, item in enumerate(sorted_entries, start=1):
    title = item.title
    link = item.link
    description = item.description
    title_to_link[str(index)] = link
    table.add_row(
        str(index),
        Padding(title, (1, 0)),
        Padding(description, (1, 0))
    )

console.print(table)

# Navegação nos títulos para acessar os links...
chosen_index = Prompt.ask("Digite o número do título que deseja acessar (ou 'sair' para sair):")

while chosen_index.lower() != "sair":
    if chosen_index in title_to_link:
        console.print(f"Acessando link para '{sorted_entries[int(chosen_index) - 1].title}': {title_to_link[chosen_index]}")
    else:
        console.print("Número do título não encontrado.")

    chosen_index = Prompt.ask("Digite outro número do título que deseja acessar (ou 'sair' para sair):")
