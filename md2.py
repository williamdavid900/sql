MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item

[bold red]This is bold red.[/bold red]
"""
from rich.console import Console
from rich.markdown import Markdown
from rich import print as cprint

console = Console()
# md = Markdown(MARKDOWN)
md = Markdown('[cyan]this is ****bold**** text[/cyan]')

console.print('this [green]is a test')
md = Markdown('[cyan]this is ****bold**** text[/cyan]')
cprint("[bold red]alert![/bold red] Something happened")

