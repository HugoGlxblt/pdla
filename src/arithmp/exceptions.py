"""
Custom exceptions thrown by the parser.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Final


@dataclass(frozen=True)
class ParserExceptionContext:
    """
    Context information for parser exceptions.
    """

    filepath: Path | None
    line: int
    column: int
    source: str


class ParserException(Exception):
    """
    Custom exception for parser errors.
    """

    def __init__(self, message: str, context: ParserExceptionContext) -> None:
        """
        Initialize the exception with the context and an error message.
        """
        super().__init__(message)

        self.context: Final = context


class SyntaxException(ParserException):
    """
    Exception raised for syntax errors in the parser.
    """


class ImportException(ParserException):
    """
    Exception raised when an import operation fails.
    """

    def __init__(
        self, module: str, message: str, context: ParserExceptionContext
    ) -> None:
        """
        Initialize the exception with the file path and an error message.
        """
        super().__init__(f"failed to import '{module}': {message}", context)
        self.module = module
        self.message = message


class IncludeException(ParserException):
    """
    Exception raised when an include operation fails.
    """

    def __init__(
        self, include_filepath: Path, message: str, context: ParserExceptionContext
    ) -> None:
        """
        Initialize the exception with the file path and an error message.
        """
        super().__init__(f"failed to include '{include_filepath}': {message}", context)
        self.include_filepath = include_filepath
        self.message = message


class ZeroDivisionException(ParserException):
    """
    Exception raised when a division by zero is attempted.
    """


class UndefinedVariableException(ParserException):
    """
    Exception raised when an undefined variable is accessed.
    """

    def __init__(self, variable_name: str, context: ParserExceptionContext) -> None:
        """
        Initialize the exception with the variable name.
        """
        super().__init__(f"undefined variable '{variable_name}'", context)
        self.variable_name = variable_name


class UndefinedFunctionException(ParserException):
    """
    Exception raised when an undefined function is called.
    """

    def __init__(self, function_name: str, context: ParserExceptionContext) -> None:
        """
        Initialize the exception with the function name.
        """
        super().__init__(f"undefined function '{function_name}'", context)
        self.function_name = function_name


class BadFunctionCallException(ParserException):
    """
    Exception raised when a function is called with incorrect arguments.
    """

    def __init__(
        self, function_name: str, message: str, context: ParserExceptionContext
    ) -> None:
        """
        Initialize the exception with the function name and an error message.
        """
        super().__init__(f"bad function call '{function_name}': {message}", context)
        self.function_name = function_name
        self.message = message
