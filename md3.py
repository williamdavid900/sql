from rich.console import Console
from rich.markdown import Markdown
from rich import print as rprint

msg = 'this **[green]**is a test'
console = Console()
md = Markdown(msg)
rprint(md)

# rprint(Markdown(msg))
exit()
console.print(Markdown(msg))
# md Mar=kdown
class MyObject:
    def __rich__(self) -> str:
        return txt

txt = "[bold blue]MyObject() **some** markdown"
my = MyObject()

rprint(my)

rprint("[bold red]***italicalert!***[/bold red] Something happened")

