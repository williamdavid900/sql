from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

console = Console()
markdown = Markdown(
"""
# Combining Markdown and Rich

This is an example of how to combine the power of Markdown with Rich's formatting:

This is **simple** markdown.

* **Bold** text
* *Italic* text
* [Link to Google](https://www.google.com)
* `Inline code`

You can even embed formatted tables or progress bars within your Markdown:

| Column 1 | Column 2 |
|---|---|
| Value 1 | Value 2 |

[progress.bar]
"""
)

console.print(Panel(markdown, title="Rich Markdown"))

highlighted_text = Text("This text is highlighted!", style="bold magenta")
console.print(highlighted_text)
