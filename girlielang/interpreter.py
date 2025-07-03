from .errors import GirlieLangError, BreakSignal, ContinueSignal

variables = {}
functions = {}

def eval_expr(expr):
    """Evaluate an expression in the current variable scope."""
    try:
        return eval(expr, {}, {**variables, **functions})
    except Exception:
        raise GirlieLangError(f"Couldn't evaluate: {expr}")
def run_program(statements):
    """Run an list of statements."""
    global variables, functions
    i = 0
    while i < len(statements):
        stmt = statements[i]

        if stmt['type'] == 'assign':
            # girly = 10
            variables[stmt['var']] = eval_expr(stmt['value'])

        elif stmt['type'] == 'print':
            # gasp / print
            value = eval_expr(stmt['value'])
            print(value)

        elif stmt['type'] == 'input':
            # wyd / input
            variables[stmt['var']] = input(stmt['prompt'])

        elif stmt['type'] == 'if':
            # istg / if
            cond = eval_expr(stmt['condition'])
            if cond:
                run_program(stmt['body'])
            elif stmt.get('orelse'):
                run_program(stmt['orelse'])

        elif stmt['type'] == 'while':
            # while condition
            while eval_expr(stmt['condition']):
                try:
                    run_program(stmt['body'])
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif stmt['type'] == 'for':
            # for i from x to y
            loop_var = stmt['var']
            start = eval_expr(stmt['start'])
            end = eval_expr(stmt['end'])

            for v in range(start, end):
                variables[loop_var] = v
                try:
                    run_program(stmt['body'])
                except BreakSignal:
                    break
                except ContinueSignal:
                    continue

        elif stmt['type'] == 'function_def':
            # omg bestie() {..}
            functions[stmt['name']] = {
                'params': stmt['params'],
                'body': stmt['body']
            }

        elif stmt['type'] == 'function_call':
            # bestie(10, 20)
            func = functions.get(stmt['name'])
            if not func:
                raise GirlieLangError(f"OMG! No such function: {stmt['name']}")

            args = stmt['args']
            params = func['params']
            if len(args) != len(params):
                raise GirlieLangError("Mismatch in function arguments")

            # Save current scope
            old_vars = variables.copy()
            for p, a in zip(params, args):
                variables[p] = eval_expr(a)

            try:
                run_program(func['body'])
            finally:
                # Restore old scope no matter what
                variables.clear()
                variables.update(old_vars)

        elif stmt['type'] == 'return':
            # returning early
            return eval_expr(stmt['value'])

        elif stmt['type'] == 'break':
            raise BreakSignal()

        elif stmt['type'] == 'continue':
            raise ContinueSignal()

        elif stmt['type'] == 'expression':
            # Handle standalone expressions/function calls
            if 'name' in stmt and 'args' in stmt:
                # This is actually a function call
                func = functions.get(stmt['name'])
                if not func:
                    raise GirlieLangError(f"OMG! No such function: {stmt['name']}")

                args = stmt['args']
                params = func['params']
                if len(args) != len(params):
                    raise GirlieLangError("Mismatch in function arguments")

                # Save current scope
                old_vars = variables.copy()
                for p, a in zip(params, args):
                    variables[p] = eval_expr(a)

                try:
                    run_program(func['body'])
                finally:
                    # Restore old scope no matter what
                    variables.clear()
                    variables.update(old_vars)
            else:
                # Just evaluate the expression
                eval_expr(stmt['value'])

        i += 1