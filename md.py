MARKDOWN = """
# h1
## h2
### h3
#### h4
[red]
here is **bold** text
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)
