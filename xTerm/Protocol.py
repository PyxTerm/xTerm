from typing import Any, cast, Set, TYPE_CHECKING
from inspect import isclass

if TYPE_CHECKING:
    from .Console import RenderableType

_GIBBERISH = """aihwerij235234ljsdnp34ksodfipwoe234234jlskjdf"""


def is_renderable(check_object: Any) -> bool:
    """Check if an object may be rendered by Rich."""
    return (
        isinstance(check_object, str)
        or hasattr(check_object, "__xTerm__")
        or hasattr(check_object, "__xTerm_Console__")
    )


def rich_cast(renderable: object) -> "RenderableType":
    """Cast an object to a renderable by calling __xTerm__ if present.

    Args:
        renderable (object): A potentially renderable object

    Returns:
        object: The result of recursively calling __xTerm__.
    """
    from .Console import RenderableType

    rich_visited_set: Set[type] = set()  # Prevent potential infinite loop
    while hasattr(renderable, "__xTerm__") and not isclass(renderable):
        # Detect object which claim to have all the attributes
        if hasattr(renderable, _GIBBERISH):
            return repr(renderable)
        cast_method = getattr(renderable, "__xTerm__")
        renderable = cast_method()
        renderable_type = type(renderable)
        if renderable_type in rich_visited_set:
            break
        rich_visited_set.add(renderable_type)

    return cast(RenderableType, renderable)
