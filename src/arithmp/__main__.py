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

    if c is not None:
        try:
            result = parser.parse(None, c)
            if result is not None:
                click.echo(result)
        except ParserException as e:
            click.echo(
                f"Error in expression at line {e.context.line} column {e.context.column} '{e.context.source}': {e}'"
            )
        return

    if filepath is not None:
        try:
            result = parser.parse(filepath, filepath.read_text())
            if result is not None:
                click.echo(result)
        except ParserException as e:
            click.echo(
                f"Error in script '{filepath}' at line {e.context.line} column {e.context.column} '{e.context.source}': {e}'"
            )
        return

    click.echo("Arithmp Interactive Interpreter. Press Ctrl+D or Ctrl+C to exit.")
    while True:
        try:
            expression = input("arithmp> ")
            if not expression.strip():
                continue

            result = parser.parse(None, expression)
            if result is not None:
                click.echo(result)

        except EOFError:
            click.echo()
            break
        except KeyboardInterrupt:
            click.echo()
            break
        except ParserException as e:
            click.echo(f"Error: {e}")


if __name__ == "__main__":
    main()
