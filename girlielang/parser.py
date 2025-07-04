import re 
from .errors import GirlieSyntaxError

# Boolean mappings
BOOLEAN_LITERALS = {
    'slayed': 'True',
    'nope': 'False'
}

BOOLEAN_REPLACEMENTS = {
    ' naur ': ' not ',
    ' whatever ': ' or ',
    ' and ': ' and '
}

#utils 
def is_identifier(token: str) -> bool :
    return token.isidentifier()

def to_literal(value: str):
    if value.lower() == "slayed":
        return True 
    elif value.lower() == "nope":  # Fixed: was "naur" but should be "nope"
        return False
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value.strip('"').strip("'")  # return as string if not a number

# Language keywords 
KEYWORDS = {
        "gasp", "wyd", "ykw?", "istg", "else", "elif",
            "girl!", "while", "do while", "stawp", "go girlie", "bye",
                "OMG", "ate", "hey girlie <3", "byee hg </3"
}

# Token matcher 
TOKEN_REGEX = re.compile(r"""
     (\".*?\")|                       # double-quoted strings
     (\d+)|                           # numbers
     (ykw\?)|                         # declaration keyword
     ([a-zA-Z_][a-zA-Z0-9_]*)|        # identifiers (fallback)
     (==|!=|<=|>=|<|>|=)|             # comparison / assignment ops
     (\+|\-|\*|\/|%)|                 # arithmetic ops
     (\(|\)|:)|                       # grouping tokens
     (\s+)|                           # whitespace (ignored)
      (.)                              # catch-all for unexpected chars
 """, re.VERBOSE)

# Token wrapper for type/value pair
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"

# raw code into tokens
def tokenize(source_code):
    tokens = []
    
    for match in TOKEN_REGEX.finditer(source_code):
        string, number, decl_kw, ident, comp, arith, group, whitespace, other = match.groups()
        
        if string:
            tokens.append(Token("STRING", string.strip('"')))
        elif number:
            tokens.append(Token("NUMBER", int(number)))
        elif decl_kw:
            tokens.append(Token("DECL", decl_kw))
        elif ident:
            token_type = "KEYWORD" if ident in KEYWORDS else "IDENT"
            tokens.append(Token(token_type, ident))
        elif comp:
            tokens.append(Token("OP", comp))
        elif arith:
            tokens.append(Token("ARITH", arith))
        elif group:
            tokens.append(Token("GROUP", group))
        elif whitespace:
            continue  # ignore whitespace
        elif other:
            raise GirlieSyntaxError(f"Unexpected character: '{other}'")

    return tokens

# Breaks full source into indi line statements and builds intermediate rep
def parse_statements(source_code):
    lines = source_code.strip().split('\n')
    return parse_block(lines, 0, 0)[0]

def parse_block(lines, start_index, base_indent):
    instructions = []
    i = start_index
    pending_if = None  # Used to attach elif/else to the last if block

    while i < len(lines):
        raw_line = lines[i]
        line = raw_line.strip()
        indent = len(raw_line) - len(line)

        # Skip blank lines and comments
        if not line or line.startswith("#"):
            i += 1
            continue

        # Exit current block
        if indent < base_indent:
            break
        elif indent > base_indent:
            raise GirlieSyntaxError(f"Unexpected indent at line {i + 1}: {lines[i]}")

        # Replace booleans and ops
        for literal, repl in BOOLEAN_LITERALS.items():
            line = re.sub(rf'\b{literal}\b', repl, line)
        for slang, op in BOOLEAN_REPLACEMENTS.items():
            line = line.replace(slang, op)

        # Conditional blocks
        if line.startswith("istg"):
            condition = line[len("istg"):].strip()
            if condition.endswith(":"):
                condition = condition[:-1].strip()  # trailing colon
            body, next_i = parse_block(lines, i + 1, base_indent + 4)
            if_block = {
                "type": "if",
                "condition": condition,
                "body": body,
                "orelse": []
            }
            instructions.append(if_block)
            pending_if = if_block
            i = next_i
            continue
        if line.startswith("elif"):
            if pending_if is None:
                raise GirlieSyntaxError(f"'elif' without preceding 'istg' at line {i + 1}")
            condition = line[len("elif"):].strip()
            if condition.endswith(":"):
                condition = condition[:-1].strip()  #trailing colon
            body, next_i = parse_block(lines, i + 1, base_indent + 4)
            pending_if['orelse'].append({
                "type": "if",
                "condition": condition,
                "body": body,
                "orelse": []
            })
            pending_if = pending_if['orelse'][-1]  # Allow chaining
            i = next_i
            continue
        if line.startswith("else"):
            if pending_if is None:
                raise GirlieSyntaxError(f"'else' without preceding 'istg' at line {i + 1}")
            body, next_i = parse_block(lines, i + 1, base_indent + 4)
            pending_if['orelse'] = body  
            pending_if = None
            i = next_i
            continue
        # Loops
        if line.startswith("while"):
            condition = line[len("while"):].strip()
            if condition.endswith(":"):
                condition = condition[:-1].strip()  #trailing colon
            body, next_i = parse_block(lines, i + 1, base_indent + 4)
            instructions.append({
                "type": "while",
                "condition": condition,
                "body": body
            })
            i = next_i
            continue
        if line.startswith("girl!"):
            # girl! i in start to end
            stmt = line[len("girl!"):].strip()
            if stmt.endswith(":"):
                stmt = stmt[:-1].strip()  # trailing colon
            match = re.match(r'(\w+)\s+in\s+(.+)\s+to\s+(.+)', stmt)
            if not match:
                raise GirlieSyntaxError(f"Invalid for loop syntax at line {i + 1}")
            var, start, end = match.groups()
            body, next_i = parse_block(lines, i + 1, base_indent + 4)
            instructions.append({
                "type": "for",
                "var": var,
                "start": start,
                "end": end,
                "body": body
            })
            i = next_i
            continue
        # Functions
        if line.startswith("OMG"):
            sig = line[len("OMG"):].strip()
            if sig.endswith(":"):
                sig = sig[:-1].strip()  #trailing colon
            match = re.match(r'(\w+)\((.*?)\)', sig)
            if not match:
                raise GirlieSyntaxError(f"Invalid function definition at line {i + 1}")
            name, params = match.groups()
            param_list = [p.strip() for p in params.split(',')] if params else []
            body, next_i = parse_block(lines, i + 1, base_indent + 4)
            instructions.append({
                "type": "function_def",
                "name": name,
                "params": param_list,
                "body": body
            })
            i = next_i
            continue
        # Singleline statement 
        instructions.append(parse_single_line(line))
        i += 1

    return instructions, i

def parse_single_line(line):
    if line.startswith("ykw?"):
        var_name, value = _parse_assignment(line)
        return {"type": "assign", "var": var_name, "value": value}

    if line.startswith("gasp"):
        return {
            "type": "print",
            "value": line[len("gasp"):].strip()
        }

    if line.startswith("wyd"):
        parts = line[len("wyd"):].strip().split(" ", 1)
        if len(parts) != 2:
            raise GirlieSyntaxError("Invalid 'wyd' syntax. Use: wyd <var> \"prompt\"")
        var, prompt = parts
        return {
            "type": "input",
            "var": var.strip(),
            "prompt": prompt.strip().strip('"')
        }


    if line.startswith("ate"):
        return {
            "type": "return",
            "value": line[len("ate"):].strip()
        }

    if line == "hey girlie <3":
        return {"type": "start"}

    if line == "byee hg </3":
        return {"type": "end"}

    if line == "stawp":
        return {"type": "break"}

    if line == "go girlie":
        return {"type": "continue"}

    if line == "bye":
        return {"type": "endloop"}

    # Check for function calls 
    func_call_match = re.match(r'(\w+)\((.*?)\)', line)
    if func_call_match:
        func_name, args_str = func_call_match.groups()
        args = [arg.strip() for arg in args_str.split(',')] if args_str.strip() else []
        return {
            "type": "function_call",
            "name": func_name,
            "args": args
        }

    return {
        "type": "expression",
        "value": line
    }

def _parse_assignment(line):
    if "=" not in line:
        raise GirlieSyntaxError("Assignment must include '='")

    var_part, *value_parts = line.split("=")
    var_name = var_part.replace("ykw?", "").strip()
    value = "=".join(value_parts).strip()

    if not var_name:
        raise GirlieSyntaxError("Missing variable name in declaration")
    if not value:
        raise GirlieSyntaxError("Missing value in assignment")

    return var_name, value