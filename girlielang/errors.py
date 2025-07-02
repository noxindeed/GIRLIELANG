
class GirlieLangError(Exception):
    """Base exception for all GirlieLang errors."""
    pass

class GirlieSyntaxError(GirlieLangError):
    """Raised when there's a syntax error in the code."""
    def __init__(self, message, line=None):
        decorated = f"omg syntax error!!  {message}"
        if line is not None:
            decorated = f"[line {line}] " + decorated
        super().__init__(decorated)
                                             

class GirlieRuntimeError(GirlieLangError):
    """Raised when a runtime error occurs."""
    def __init__(self, message, context=None):
        decorated = f"girl help!! runtime issue  {message}"
        if context:
            decorated = f"{context}  " + decorated
        super().__init__(decorated)


class GirlieNameError(GirlieLangError):
    """Raised when a variable or fun name is not found."""
    def __init__(self, name):
        super().__init__(f"uhhh who's '{name}'???  (NameError)")


class GirlieTypeError(GirlieLangError):
    """Raised when theres a type mismatch or unsupported operation."""
    def __init__(self, message):
        super().__init__(f"no bestie  that's a type problem  {message}")