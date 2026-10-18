"""
Custom storage for variables, including type definitions and helper functions.
"""

from __future__ import annotations

from types import NoneType

type VariableType = NoneType | bool | int | float | complex | str


class Variables:
    """
    Store variables with optional parent-scope lookup.
    """

    def __init__(
        self, variables: dict[str, VariableType], parent: Variables | None = None
    ) -> None:
        """
        Initialize this scope with local variables and an optional parent.
        """
        self._variables = variables
        self._parent = parent

    @property
    def parent(self) -> Variables | None:
        """
        The parent scope of this variable container, if any.
        """
        return self._parent

    def __contains__(self, name: str) -> bool:
        """
        Check if a variable exists in this scope or its parent scopes.
        """
        return name in self._variables or (
            self._parent is not None and name in self._parent
        )

    def __getitem__(self, name: str) -> VariableType:
        """
        Return a variable from this scope or its parent scopes.
        """
        if name in self._variables:
            return self._variables[name]
        elif self._parent is not None:
            return self._parent[name]
        else:
            raise KeyError(name)

    def __setitem__(self, name: str, value: VariableType) -> None:
        """
        Set a variable in this scope.
        """
        self._variables[name] = value

    def __delitem__(self, name: str) -> None:
        """
        Delete a variable from this scope.
        """
        if name in self._variables:
            del self._variables[name]
        else:
            raise KeyError(name)
