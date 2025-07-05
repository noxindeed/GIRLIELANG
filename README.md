#  **GIRLIELANG** 

GIRLIELANG is my fun, satirical and and ironical take on making an Esoteric Programming language purely for the sake of it.
In a nutshell, its a tiktok girlie themed language that makes use of modern tiktok genz teenage girl slang for programming.

##  Features

- **Syntax**: Uses fun slang terms like `istg`, `ykw?`, `gasp`, `OMG` as keywords

- **Full Programming Language**: Supports variables, functions, loops, conditionals, and more
- **Python-like Structure**: Indentation-based blocks similar to Python
-  **Interactive & File Mode**: Run files or use interactive REPL
-  **Custom Error Messages**: Themed error messages that match the language aesthetic
##  Getting Started

### Installation
```bash
git clone https://github.com/noxindeed/GIRLIELANG/
cd girlielang
```

### Running GirlieLang
```bash
# Run a file
python main.py <your_file>.girlie

# Interactive mode
python main.py
```

##  Syntax Overview 

### 1. Variables & Assignment

**Syntax**: `ykw?` <variable_name> = value

Example code:
```girlie
# Variable declarations
ykw? name = "Bestie"
ykw? age = 21
ykw? height = 5.6
```

### 2. Input & Output

#### Print Statement
**Syntax**: `gasp` <expression\> 

Example code:
```girlie
gasp "Hello World!"
gasp name
gasp age + 5
gasp "My name is " + name
```

#### Input Statement
**Syntax**: `wyd` <variable_name>

Example code:
```girlie
wyd username
gasp "Hello " + username
```

### 3. Conditionals

**Syntax**: 
- if - `istg` <condition\>:
- else if - `elif` <condition\> :
- else - `else`: 

Example code:
```
hey girlie <3

ykw? score = 85

istg score >= 90:
    gasp "A grade! Slayed!"
elif score >= 80:
    gasp "B grade! Pretty good bestie"
elif score >= 70:
    gasp "C grade! Could be better"
else:
    gasp "Need to study more girl!"

bye hg </3
```

### 4. Loops

#### For Loop
**Syntax**: `girl!` <variable\> in <start\> to <end\> :

Example code:
```
# Print numbers 1 to 5
girl! i in 1 to 6:
    gasp i

# Nested loops
girl! row in 1 to 4:
    girl! col in 1 to 4:
        gasp row * col
```

#### While Loop
**Syntax**: `while` <condition\>:

Example code:
```girlie
ykw? count = 0
while count < 5:
    gasp "Count is: " + count
    ykw? count = count + 1
```

### 5. Functions

#### Function Definition
**Syntax**: `OMG` <function_name\>(parameters):

Example code:
```girlie
# Function with no parameters
OMG say_hello():
    gasp "Hello bestie!"

# Function with parameters
OMG greet(name, age):
    gasp "Hey " + name
    gasp "You are " + age + " years old"
```


#### Function Calls
Example code:
```
say_hello()
greet("Sarah", 20)

ykw? result = add(10, 5)
gasp result
```

### 6. Boolean Logic & Operators

#### Boolean Literals
- `slayed` = True
-  `nope` = False
  
- #### Boolean Operators
- `naur` = not
- `whatever` = or
- `and` = and
  
Example code:
```girlie
ykw? is_student = slayed
ykw? has_job = nope

istg is_student and naur has_job:
    gasp "Student without job"
elif is_student whatever has_job:
    gasp "Either student or has job"
```

### 7. Control Flow

#### Break and Continue
**Syntax**: 
- `go girlie` = continue
- `stawp` = break

Example code:
```girlie
girl! i in 1 to 10:
    istg i == 5:
        go girlie    # continue
    istg i == 8:
        stawp        # break
    gasp i
```

#### Return Statement
**Syntax**: `ate` <value\>

Example code:
```girlie
OMG calculate_grade(score):
    istg score >= 90:
        ate "A"
    elif score >= 80:
        ate "B"
    else:
        ate "F"
```

### 8. Program Structure

```girlie
# Program start marker (optional)
hey girlie <3

# Your code here
ykw? message = "Hello GirlieLang!"
gasp message

# Program end marker (optional)
byee hg </3
```

##  Complete Examples

### Ex1: Simple Calculator
```girlie
hey girlie <3

OMG add(a, b):
    ate a + b

OMG multiply(a, b):
    ate a * b

OMG divide(a, b):
    istg b == 0:
        gasp "Cannot divide by zero bestie!"
        ate 0
    else:
        ate a / b

# Main program
gasp "=== Girlie Calculator ==="
ykw? x = 10
ykw? y = 5

gasp "Addition: " + add(x, y)
gasp "Multiplication: " + multiply(x, y)
gasp "Division: " + divide(x, y)

byee hg </3
```

### Ex2: Number Guessing Game
```girlie
hey girlie <3

OMG guessing_game():
    ykw? secret = 7
    ykw? attempts = 0
    
    gasp "Guess the number between 1 and 10!"
    
    while attempts < 3:
        wyd guess
        ykw? attempts = attempts + 1
        
        istg guess == secret:
            gasp "OMG you got it! Slayed!"
            ate slayed
        elif guess < secret:
            gasp "Too low bestie!"
        else:
            gasp "Too high girl!"
    
    gasp "Game over! The number was " + secret
    ate nope

# Run the game
guessing_game()

byee hg </3
```

### Ex3: simple demo
```girlie
hey girlie <3

ykw? name = "nox"
ykw" age = 67
gasp name
gasp age

gasp "Maths"
ykw? x = 6
ykw? y = 7
gasp x + y

istg x > y:
    gasp "x is bigger:
else :
    gasp "y is bigger"
```


##  Language Keywords Reference

| Keyword | Standard Equivalent | Purpose |
|---------|-------------------|---------|
| `ykw?` | `var =` | Variable declaration |
| `gasp` | `print` | Output statement |
| `wyd` | `input` | Input statement |
| `istg` | `if` | Conditional statement |
| `elif` | `elif` | Else if condition |
| `else` | `else` | Else condition |
| `girl!` | `for` | For loop |
| `while` | `while` | While loop |
| `OMG` | `def` | Function definition |
| `ate` | `return` | Return statement |
| `stawp` | `break` | Break loop |
| `go girlie` | `continue` | Continue loop |
| `slayed` | `True` | Boolean true |
| `nope` | `False` | Boolean false |
| `naur` | `not` | Boolean not |
| `whatever` | `or` | Boolean or |
| `and` | `and` | Boolean and |
| `hey girlie <3` | - | Program start (optional) |
| `byee hg </3` | - | Program end (optional) |

##  Error Messages



- **Syntax Error**: `"omg syntax error!! <message>"`
- **Runtime Error**: `"girl help!! runtime issue <message>"`
- **Name Error**: `"uhhh who's 'variable'??? (NameError)"`
- **Type Error**: `"no bestie that's a type problem <message>"`
  
- ##  Technical Details

- ### Architecture
- **Parser**: Converts GirlieLang source code into an Abstract Syntax Tree
- **Interpreter**: Executes the parsed instructions
-  **Error Handler**: Manages custom error types with themed messages
  
- ### Supported Data Types
-  **Integers**: `42`, `-17`
-  **Floats**: `3.14`, `-2.5`
-  **Strings**: `"Hello World!"`, `'Single quotes'`
-  **Booleans**: `slayed` (True), `nope` (False)
  
- ### File Extension
- Use `.girlie` extension for GirlieLang source files.
  
- ##  Future Plans:
  

-  Add more data structures (arrays, objects)
-  Implement more built-in functions
-  Add file I/O operations
-  Improve error reporting with line numbers
-  Add more girly slang terms




#


   made with love by nox
