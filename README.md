![](https://raw.githubusercontent.com/Jetrom17/tab-rss/main/demo.gif)
> Demonstração do código.

Desenvolvi um script em Python 3 utilizando o RSS (Distribuição Realmente Simples) do TabNews. Com essa ferramenta, você poderá acompanhar as informações postadas no TabNews diretamente no seu CLI (Interface de Linha de Comando). Essa abordagem oferece uma maneira prática e eficiente de se manter atualizado com as últimas notícias e atualizações do TabNews sem precisar abrir um navegador. Tornando prático e peculiar.
> [!Note]
> Se estiver usando Linux, por exemplo, é possível acessar o link através do pacote `elinks`.
>
> `sudo apt install elinks`
> 
> `elinks` [URL DO POST ESCOLHIDO]

### [Estrutura]

- Baseado em TUI (Usuário de Texto baseado em Interface).
- Limpa o console automaticamente com condição de acordo com seu sistema operacional. Evitando poluição de caracteres.
- As informações estão em ordem por data, da mais recente ao mais antigo. Diferente do próprio RSS apresentado.
- Apenas checagem do que se acontece na plataforma, ok. Para ler, escolha o post desejado para ler, através do número.

### [Instalação]

```bash
git clone https://github.com/Jetrom17/tab-rss/
cd tab-rss
python3 tab-rss.py
```

> [!Important]
> Disponível no `pip` futuramente. Tornando a instalação, mais prática.
