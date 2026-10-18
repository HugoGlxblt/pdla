"""Arithmp: Command-line interface for the Arithmp package."""

from pathlib import Path

import click

from .parser import Parser, ParserException


@click.command()
@click.argument("filepath", type=click.Path(exists=True, path_type=Path))
def main(filepath: Path) -> None:
    """
    Main entry point for the Arithmp command-line interface.
    """
    parser = Parser()
    try:
        if (result := parser.parse(filepath, filepath.read_text())) is not None:
            click.echo(result)
    except ParserException as e:
        click.echo(
            f"Error in script '{filepath}' at line {e.context.line} column {e.context.column} '{e.context.source}': {e}'"
        )


if __name__ == "__main__":
    main()
