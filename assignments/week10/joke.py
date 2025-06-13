import cowsay, pyjokes
#from rich import print

from rich.console import Console

console = Console()

# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

console.print("This is the best joke you'll ever hear", style="blink bold white on red")

joke = pyjokes.get_joke()
character_joke =  cowsay.milk(joke)
