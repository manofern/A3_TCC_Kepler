# Analisador Léxico
def lexer(code):
    # Divide o código em tokens
    return code.split()

# Analisador Sintático
def parser(tokens):
    # Verifica a sintaxe
    if tokens[0] == "print":
        return "PRINT_STATEMENT"
    elif tokens[0] == "var":
        return "VARIABLE_DECLARATION"

# Tradutor
def translator(parsed_code):
    if parsed_code == "PRINT_STATEMENT":
        return "print"
    elif parsed_code == "VARIABLE_DECLARATION":
        return "var"

# Função principal
def transpile(code):
    tokens = lexer(code)
    parsed_code = parser(tokens)
    translated_code = translator(parsed_code)
    return translated_code

# Exemplo de uso
source_code = "print 'Hello, world!'"
print("Código de origem:", source_code)
print("Código traduzido:", transpile(source_code))