"""Arithmp: Command-line interface for the Arithmp package."""

from pathlib import Path

import click

from .parser import Parser, ParserException


@click.command()
@click.option("-c", type=str, help="Evaluate the given arithmetic expression.")
@click.argument(
    "filepath", type=click.Path(exists=True, path_type=Path), required=False
)
def main(c: str | None, filepath: Path | None) -> None:
    """
    Main entry point for the Arithmp command-line interface.
    """
    parser = Parser()

    try:
        if c is not None:
            result = parser.parse(None, c)
        elif filepath is not None:
            result = parser.parse(filepath, filepath.read_text())
        else:
            result = None

        if result is not None:
            click.echo(result)

    except ParserException as e:
        source_name = (
            f"script '{e.context.filepath}'" if e.context.filepath else "expression"
        )
        click.echo(
            f"Error in {source_name} at line {e.context.line} column {e.context.column} '{e.context.source}': {e}'"
        )


if __name__ == "__main__":
    main()
