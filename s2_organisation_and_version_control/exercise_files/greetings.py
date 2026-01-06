"""
ALTERNATIVE

import typer

def greet(count:int = 1):
    [print("HELLo") for i in range(count)]


if __name__ == "__main__":
    typer.run(greet)
"""

import typer
app = typer.Typer()

@app.command()
def hello(count: int = 1, name: str = "World"):
    for x in range(count):
        typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()