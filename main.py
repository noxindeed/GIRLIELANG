
"""
GirlieLang Interpreter Main Entry Point
"""

import sys
from girlielang.parser import parse_statements
from girlielang.interpreter import run_program
from girlielang.errors import GirlieLangError

def run_file(filename):
    """Run a GirlieLang file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        print(f" Running {filename}...")
        statements = parse_statements(source_code)
        run_program(statements)
        print(" Program completed successfully!")
        
    except FileNotFoundError:
        print(f" File not found: {filename}")
    except GirlieLangError as e:
        print(f" GirlieLang Error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")

def run_interactive():
    """Run GirlieLang in interactive mode."""
    print(" Welcome to GirlieLang Interactive Mode! ")
    print("Type 'quit' to exit.")
    
    while True:
        try:
            line = input("girlie> ").strip()
            if line.lower() in ['quit', 'exit', 'bye']:
                print("byee hg </3")
                break
            
            if not line:
                continue
                
            statements = parse_statements(line)
            run_program(statements)
            
        except KeyboardInterrupt:
            print("\nbyee hg </3")
            break
        except GirlieLangError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_interactive()

if __name__ == "__main__":
    main()
