from typing import Optional, TYPE_CHECKING

from .Jupyter import JupyterMixin
from .Measure import Measurement

if TYPE_CHECKING:
    from .Console import Console, ConsoleOptions, RenderableType, RenderResult


class Constrain(JupyterMixin):
    """Constrain the width of a renderable to a given number of characters.

    Args:
        renderable (RenderableType): A renderable object.
        width (int, optional): The maximum width (in characters) to render. Defaults to 80.
    """

    def __init__(self, renderable: "RenderableType", width: Optional[int] = 80) -> None:
        self.renderable = renderable
        self.width = width

    def __xTerm_Console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult":
        if self.width is None:
            yield self.renderable
        else:
            child_options = options.update_width(min(self.width, options.max_width))
            yield from console.render(self.renderable, child_options)

    def __xTerm_Measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "Measurement":
        if self.width is not None:
            options = options.update_width(self.width)
        measurement = Measurement.get(console, options, self.renderable)
        return measurement
