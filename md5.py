from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

console = Console()
markdown = Markdown(
"""
This is **simple** markdown.
"""
)

console.print(Panel(markdown, title="Rich Markdown"), style="bold red" )

highlighted_text = Text("This text is highlighted!", style="bold green")
import pprint
pprint.pprint(highlighted_text)
