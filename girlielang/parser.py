import re 
from errors import GirlieSyntaxError

#utils 
def is_identifier(token: str) -> bool :
    return token.isidentifier()

def to_literal(value: str):
    if value.lower() == "slayed":
        return True 
    elif value.lower() == "naur":
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

# Breaks full source into individual line statements and builds intermediate representation
def parse_statements(source_code):
    instructions = []
    for raw_line in source_code.strip().split("\n"):
        line = raw_line.strip()

        # skip blank lines and comments
        if not line or line.startswith("#"):
            continue

        # Handle variable declarations
        if line.startswith("ykw?"):
            var_name, value = _parse_assignment(line)
            instructions.append({"type": "assign", "var": var_name, "value": value})

        # Print expression
        elif line.startswith("gasp"):
            expression = line[len("gasp"):].strip()
            instructions.append({"type": "print", "expr": expression})

        # User input assignment
        elif line.startswith("wyd"):
            var_name = line[len("wyd"):].strip()
            instructions.append({"type": "input", "var": var_name})

        # Function definition start
        elif line.startswith("OMG"):
            fn_name = line[len("OMG"):].strip()
            instructions.append({"type": "function_def", "name": fn_name})

        # Function return value
        elif line.startswith("ate"):
            return_val = line[len("ate"):].strip()
            instructions.append({"type": "return", "value": return_val})

        # Program entry point
        elif line == "hey girlie <3":
            instructions.append({"type": "start"})

        # Program end
        elif line == "byee hg </3":
            instructions.append({"type": "end"})

        # Conditionals
        elif line.startswith("istg"):
            condition = line[len("istg"):].strip()
            instructions.append({"type": "if", "cond": condition})

        elif line.startswith("elif"):
            condition = line[len("elif"):].strip()
            instructions.append({"type": "elif", "cond": condition})

        elif line.startswith("else"):
            instructions.append({"type": "else"})

        # Loop constructs
        elif line.startswith("girl!"):
            for_expr = line[len("girl!"):].strip()
            instructions.append({"type": "for", "stmt": for_expr})

        elif line.startswith("while"):
            condition = line[len("while"):].strip()
            instructions.append({"type": "while", "cond": condition})

        elif line.startswith("do while"):
            condition = line[len("do while"):].strip()
            instructions.append({"type": "do_while", "cond": condition})

        # Loop control
        elif line == "stawp":
            instructions.append({"type": "break"})

        elif line == "go girlie":
            instructions.append({"type": "continue"})

        elif line == "bye":
            instructions.append({"type": "endloop"})

        # Fallback: treat unknown line as generic expression
        else:
            instructions.append({"type": "expression", "value": line})

    return instructions

# Parses assignment expressions like: ykw? var = a
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