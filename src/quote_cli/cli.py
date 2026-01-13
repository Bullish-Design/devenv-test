# src/quote_cli/cli.py
from __future__ import annotations

import random

import typer

from quote_cli.quotes import create_default_collection

app = typer.Typer(help="Display random inspirational quotes")


@app.command()
def main() -> None:
    """Display a random quote."""
    collection = create_default_collection()
    quotes = collection.get_all()
    quote = random.choice(quotes)
    typer.echo(quote.format())


if __name__ == "__main__":
    app()
