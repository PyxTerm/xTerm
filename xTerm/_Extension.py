from typing import Any


def load_ipython_extension(ip: Any) -> None:  # pragma: no cover
    # prevent circular import
    from .Pretty import install
    from .Traceback import install as tr_install

    install()
    tr_install()
