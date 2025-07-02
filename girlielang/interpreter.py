from errors import GirlieLangError, BreakSignal, ContinueSignal

varsfunctions = {}

def eval_expr(expr):
    """Evaluate an expression in the current variable scope."""
    try:
        return eval(expr, {}, varsfunctions)
    except Exception:
        raise GirlieLangError(f"Couldn't evaluate: {expr}")