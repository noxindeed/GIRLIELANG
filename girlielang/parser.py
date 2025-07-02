import re 
from errors import GirlieSyntaxError

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