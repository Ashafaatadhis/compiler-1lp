import sys
from lexer import OneLLexer
from parser import OneLParser
from interpreter import Interpreter

def run(code):
    lexer = OneLLexer()
    parser = OneLParser()
    interpreter = Interpreter()

    tokens = lexer.tokenize(code)
    ast = parser.parse(tokens)
    interpreter.eval_stm(ast)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename.1l>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    run(source)
