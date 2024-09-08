from abc import ABC


class RichRenderable(ABC):
    """An abstract base class for xTerm renderables.

    Note that there is no need to extend this class, the intended use is to check if an
    object supports the xTerm renderable protocol. For example::

        if isinstance(my_object, RichRenderable):
            console.print(my_object)

    """

    @classmethod
    def __subclasshook__(cls, other: type) -> bool:
        """Check if this class supports the xTerm render protocol."""
        return hasattr(other, "__xTerm_Console__") or hasattr(other, "__xTerm__")


if __name__ == "__main__":  # pragma: no cover
    from .Text import Text

    t = Text()
    print(isinstance(Text, RichRenderable))
    print(isinstance(t, RichRenderable))

    class Foo:
        pass

    f = Foo()
    print(isinstance(f, RichRenderable))
    print(isinstance("", RichRenderable))
