import ply.lex as lex
from ply import yacc
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Análise Léxica
reserved = {
   'KIF' : 'KIF',
#    'KELIF' : 'KELIF',
   'KELSE' : 'KELSE',
   'KWHILE' : 'KWHILE',
   'KOR':'KOR',
#    'KT':'KT',
#    'KF':'KF',
   'KRINT':'KRINT',
   'KINPUT':'KINPUT',
   'KRANGE':'KRANGE',
   'KIN':'KIN',
}

tokens = [
    'INTEIRO',
    'DOUBLE',
    'STRING',
    'INT',
    'VARIAVEL',
    'OP_MAT_ADICAO',
    'OP_MAT_SUB',
    'OP_MAT_MULT',
    'OP_MAT_POT',
    'OP_MAT_DIV',
    'OP_EXEC_VIRGULA',
    'OP_ATRIB_IGUAL',
    'OP_ATRIB_MAIS_IGUAL',
    'OP_REL_DUPLO_IGUAL',
    'OP_REL_MENOR',
    'OP_REL_MAIOR',
    'OP_FINAL_LINHA_PONTO_VIRGULA', 
    'OP_PRIO_ABRE_PARENTESES',
    'OP_PRIO_FECHA_PARENTESES',
    #'OP_PRIO_ABRE_COLCHETES',
    #'OP_PRIO_FECHA_COLCHETES',
    'OP_PRIO_ABRE_CHAVES',
    'OP_PRIO_FECHA_CHAVES',
] + list(reserved.values())  # Concatenando com as palavras reservadas para verificação

# Regras de expressão regular (RegEx) para tokens simples

t_KWHILE = r'KWHILE'
t_KIF = r'KIF'
# t_KELIF = r'KELIF'
t_KELSE = r'KELSE'
t_KOR = r'KOR'
# t_KT = r'KT'
# t_KF = r'KF'
t_KRINT = r'KRINT'
t_KINPUT = r'KINPUT'
t_KIN = r'KIN'
t_KRANGE = r'KRANGE'

t_OP_MAT_ADICAO = r'\+'
t_OP_MAT_SUB = r'-'
t_OP_MAT_MULT = r'\*'
t_OP_MAT_POT = r'\*\*'
t_OP_MAT_DIV = r'/'
t_OP_FINAL_LINHA_PONTO_VIRGULA = r'\;'
t_OP_EXEC_VIRGULA = r'\,'
t_OP_ATRIB_IGUAL = r'\='
t_OP_ATRIB_MAIS_IGUAL = r'\+\='
t_OP_REL_DUPLO_IGUAL = r'\=\='
t_OP_REL_MENOR = r'\<'
t_OP_REL_MAIOR = r'\>'
t_OP_PRIO_ABRE_PARENTESES = r'\('
t_OP_PRIO_FECHA_PARENTESES = r'\)'
#t_OP_PRIO_ABRE_COLCHETES = r'\['
#t_OP_PRIO_FECHA_COLCHETES = r'\]'
t_OP_PRIO_ABRE_CHAVES = r'\{'
t_OP_PRIO_FECHA_CHAVES = r'\}'

t_ignore = ' \t'  # Ignora espaço e tabulação

# Regras de expressão regular (RegEx) para tokens mais "complexos"


def t_STRING(t):
    r'("[^"]*")'
    return t

def t_DOUBLE(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIAVEL(t):
    r'[a-z][a-z_0-9]*'
    return t

def t_INT(t):
    r'INT'
    return t

# Define uma regra para que seja possível rastrear o números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)

# Análise Sintática

def p_declaracoes_single(p):
    '''
    declaracoes : declaracao
    '''

def p_declaracoes_mult(p):
    '''
    declaracoes :  declaracao bloco
    '''

def p_bloco(p):
    '''
    bloco : OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES declaracao bloco OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES KRINT OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES KINPUT KRINT OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES KINPUT KINPUT KRINT OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES KINPUT KINPUT expr KRINT OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES KRINT param_cond OP_FINAL_LINHA_PONTO_VIRGULA OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES param_cond OP_FINAL_LINHA_PONTO_VIRGULA KRINT OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES KRINT expr OP_PRIO_FECHA_CHAVES
          
    '''

def p_declaracao_KWHILE(p):
    '''
    declaracao : KWHILE param_cond bloco
               | declaracao KWHILE param_cond bloco
    '''

def p_declaracao_KOR(p):
    '''
    declaracao : KOR VARIAVEL KIN KRANGE OP_PRIO_ABRE_PARENTESES INTEIRO OP_EXEC_VIRGULA INTEIRO OP_PRIO_FECHA_PARENTESES bloco
               | KOR VARIAVEL KIN KRANGE OP_PRIO_ABRE_PARENTESES DOUBLE OP_EXEC_VIRGULA DOUBLE OP_PRIO_FECHA_PARENTESES bloco
    '''

def p_declaracao_atribuicaoValorVariavel(p):
    '''
    declaracao : VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL STRING OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL funcao OP_FINAL_LINHA_PONTO_VIRGULA
            | param VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO
            | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE
            | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL
    '''

def p_declaracao_condicionais(p):
    '''
    declaracao : KIF param_cond bloco
               | declaracao KIF param_cond bloco
               | declaracao KIF param_cond bloco senao
               | KIF param_cond bloco senao
    '''

def p_declaracao_funcao_invocada(p):
    '''
    declaracao : funcao OP_FINAL_LINHA_PONTO_VIRGULA
               | print
               | input
    '''

def p_declaracao_definir_funcao(p):
    '''
    declaracao : funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES
    '''

def p_parametro_condicional(p):
    '''
    param_cond :  VARIAVEL OP_REL_MENOR INTEIRO
                | VARIAVEL OP_REL_MENOR DOUBLE
                | VARIAVEL OP_REL_MENOR VARIAVEL
                | VARIAVEL OP_REL_MAIOR INTEIRO
                | VARIAVEL OP_REL_MAIOR DOUBLE
                | VARIAVEL OP_REL_MAIOR VARIAVEL
                | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO
                | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE
                | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL
                | VARIAVEL OP_REL_DUPLO_IGUAL INTEIRO
                | VARIAVEL OP_REL_DUPLO_IGUAL DOUBLE
                | VARIAVEL OP_REL_DUPLO_IGUAL VARIAVEL

    '''

def p_KRINT(p):
    '''print : KRINT expr OP_FINAL_LINHA_PONTO_VIRGULA
                 | KRINT expr OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
                 | KRINT OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
                 | KRINT OP_PRIO_ABRE_PARENTESES  STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
    '''

def p_KINPUT(p):
    '''input : VARIAVEL OP_ATRIB_IGUAL KINPUT OP_PRIO_ABRE_PARENTESES expr OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
               | VARIAVEL OP_ATRIB_IGUAL param OP_PRIO_ABRE_PARENTESES KINPUT OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
               | VARIAVEL OP_ATRIB_IGUAL KINPUT OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA 
               | VARIAVEL OP_ATRIB_IGUAL KINPUT OP_PRIO_ABRE_PARENTESES STRING VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA 
    '''


def p_expressao_variavel(p):
    '''
    expr :  VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
    '''


def p_expressao_operacao(p):
    '''
    expr : expr OP_MAT_ADICAO expr
        |  expr OP_MAT_SUB expr
        |  expr OP_MAT_MULT expr
        |  expr OP_MAT_DIV expr
        |  expr OP_MAT_POT expr
    '''

def p_parametro_vazio(p):
    '''
    param_vazio :
    '''


def p_parametro(p):
    '''
    param : INTEIRO
        | INT
        | DOUBLE
        | STRING
        | VARIAVEL
    '''

def p_regra_funcao(p):
    '''
    funcao :  OP_PRIO_ABRE_PARENTESES param_vazio OP_PRIO_FECHA_PARENTESES
        |  OP_PRIO_ABRE_PARENTESES param OP_PRIO_FECHA_PARENTESES
    '''

def p_senao_se(p):
    '''
    senao : KELSE bloco
    '''
# Define a precedência e associação dos operadores matemáticos
precedence = (
    ('left', 'OP_MAT_ADICAO', 'OP_MAT_SUB'),
    ('left', 'OP_MAT_MULT', 'OP_MAT_DIV','OP_MAT_POT'),
)

errossintaticos = []
def p_error(p):
    global errossintaticos  # Adicionando global para acessar a lista de erros sintáticos
    errossintaticos.append(p)
    if p:
        print("ERRO SINTÁTICO: ", p)
    else:
        print("ERRO SINTÁTICO: erro de sintaxe desconhecido")
    print("Contexto próximo:")
    parser.errok()

parser = yacc.yacc()

erros = 0

# função padrão para adicionar as classificações dos tokens para ser impressa pelo compilador
def add_lista_saida(t, notificacao):
    saidas.append(( t.type, t.value, notificacao))

saidas = []

lexer = lex.lex()


def transpilar_codigo(codigo):
    lexer.input(codigo)
    tokens = []
    for token in lexer:
        tokens.append(token)

    # Concatenar tokens em uma única string
    codigo_tokens = " ".join([str(token.value) for token in tokens])
    print("String de tokens:", codigo_tokens)

    # Parse do código
    try:
        ast = parser.parse(codigo_tokens)
        print("Árvore de análise sintática gerada com sucesso.")

        # Análise semântica e transpilação do código
        codigo_transpilado = transpilar_para_python(codigo)

        # Exibir o código transpilado
        print("Código transpilado:")
        print(codigo_transpilado)

        return codigo_transpilado

    except Exception as e:
        print("Erro durante a transpilação:", e)
        return None
    

def transpilar_para_python(codigo_fonte):
    # Remover o ponto e vírgula no final da linha e espaços em branco subsequentes
    codigo_fonte = codigo_fonte.replace(';', '').rstrip()

    # Substituir PARA por for
    codigo_fonte = codigo_fonte.replace('KOR', 'for')

    codigo_fonte = codigo_fonte.replace('KELSE', 'else')

    # Substituir LEIA por input
    codigo_fonte = codigo_fonte.replace('KINPUT', 'input')

    # Substituir SE por if e ELSE por else
    codigo_fonte = codigo_fonte.replace('KIF', 'if')

    # Substituir ESCREVA por print
    codigo_fonte = codigo_fonte.replace('KRINT', 'print')

    # Substituir chaves por indentação
    codigo_fonte = codigo_fonte.replace('{', '').replace('}', '')

    # Remover ':' após a linha 'x = 11'
    codigo_fonte = codigo_fonte.replace('x = 11\n:', 'x = 11\n')

    # Substituir acentos
    codigo_fonte = codigo_fonte.replace('eh', 'é')

    # Corrigir formatação da string dentro da função ESCREVA
    in_string = False
    temp = ''
    word = ''
    for char in codigo_fonte:
        if char == '"':
            in_string = not in_string
        if not in_string:
            if char.isalpha():
                word += char
            else:
                if word == 'KRANGE':
                    temp += 'range'
                elif word == 'KIN':
                    temp += 'in'
                elif word == 'INT':
                    temp += 'int'
                else:
                    temp += word
                word = ''
                temp += char
        else:
            temp += char
    codigo_fonte = temp

    # Transpilar a estrutura ENQUANTO
    codigo_fonte = codigo_fonte.replace('KWHILE', 'while')

    # Transpilar atribuição de valor a uma variável
    codigo_fonte = codigo_fonte.replace('OP_ATRIB_IGUAL', '=')

    # Corrigir indentação
    linhas = codigo_fonte.split('\n')
    for i in range(len(linhas)):
        linha = linhas[i].strip()
        if linha.startswith(('if', 'else', 'while', 'for')):
            # Adicionar ':' se ainda não estiver presente
            if not linha.endswith(':'):
                linhas[i] = linha + ':'
        # Corrigir indentação do bloco else
        elif linha.startswith('else'):
            if i > 0 and linhas[i-1].strip().endswith(':'):
                linhas[i] = ' ' + linha
            else:
                if i+1 < len(linhas) and not linhas[i+1].strip().startswith('print'):
                    linhas[i+1] = '    ' + linhas[i+1]
                    linhas[i] = ' ' + linha

    codigo_fonte = '\n'.join(linhas)

    return codigo_fonte  

def abrir_arquivo():
    arquivo_path = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if arquivo_path:
        with open(arquivo_path, 'r') as file:
            conteudo = file.read()
            entrada_textbox.insert(ctk.END, conteudo)


def transpilar():
    # Obter o código original
    codigo_original = entrada_textbox.get("1.0", ctk.END).strip()
    
    # Realizar a análise léxica
    lexer.input(codigo_original)
    tokens = []
    for token in lexer:
        tokens.append(token)
        # Adicionar informações do token à área de texto de análise
        if token.type in reserved.values():
            notificacao = "palavra reservada"
        else:
            notificacao = ""
        linha = f"{token.type:<20} {token.value:<20} {notificacao:<20}\n"
        tabela_treeview.insert("", "end", values=(token.type, token.value, notificacao))
    
    # Transpilar o código e exibir na área de texto de saída
    resultado_transpilacao = transpilar_codigo(codigo_original)
    if resultado_transpilacao is not None:
        saida_textbox.configure(state=ctk.NORMAL)
        saida_textbox.delete("1.0", ctk.END)
        saida_textbox.insert(ctk.END, resultado_transpilacao)
        saida_textbox.configure(state=ctk.DISABLED)
    else:
        saida_textbox.configure(state=ctk.NORMAL)
        saida_textbox.delete("1.0", ctk.END)
        saida_textbox.insert(ctk.END, "Erro durante a transpilação. Verifique o código.")
        saida_textbox.configure(state=ctk.DISABLED)


def limpar():
    entrada_textbox.delete("1.0", ctk.END)
    saida_textbox.configure(state=ctk.NORMAL)
    saida_textbox.delete("1.0", ctk.END)
    saida_textbox.configure(state=ctk.DISABLED)
    for item in tabela_treeview.get_children():
        tabela_treeview.delete(item)


root = ctk.CTk()
root.geometry("900x700")
root.title("Transpilador")
root._set_appearance_mode("dark")

# Container para as telas
container = ctk.CTkFrame(root, fg_color="#242424", bg_color="#242424")
container.grid(row=1, column=0, columnspan=2, padx=(18, 18), pady=(8, 0), sticky="n")

# Configurar peso da linha para expansão vertical
container.rowconfigure(0, weight=1)

# Tela de entrada
entrada_textbox = ctk.CTkTextbox(container, width=420, height=300, fg_color="#2a2d2e", text_color="white", font=("Helvetica", 13))
entrada_textbox.grid(row=1, column=0, padx=(0, 10), pady=(0,0))

texto_codigo_fonte = ctk.CTkLabel(container, text="Código Fonte", font=("Helvetica", 15), text_color="white")
texto_codigo_fonte.grid(row=0, column=0, padx=10, pady=(0,0), sticky="n")
texto_codigo_fonte.rowconfigure(1, weight=2)

# Tela de saída
saida_textbox = ctk.CTkTextbox(container,width=420, height=300, fg_color="#2a2d2e", text_color="white", font=("Helvetica", 13), state=ctk.DISABLED)
saida_textbox.grid(row=1, column=2, padx=(10, 0), pady=(0,0))

texto_codigo_transpilado = ctk.CTkLabel(container, text="Código Transpilado", font=("Helvetica", 15), text_color="white")
texto_codigo_transpilado.grid(row=0, column=2, padx=10, pady=(0,0), sticky="n")
texto_codigo_transpilado.rowconfigure(1, weight=2)

# Configurar peso das colunas para expansão horizontal
container.columnconfigure(0, weight=1)
container.columnconfigure(1, weight=1)

container.grid_rowconfigure(0, weight=3)
container.grid_rowconfigure(1, weight=1)

# Adicionar um frame para a tabela
frame_tabela = ctk.CTkFrame(root, width=50, height=10, fg_color="#242424", bg_color="#242424")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=(70, 0), sticky="ew")
frame_tabela.rowconfigure(0, weight=1)

texto_analise_lexica = ctk.CTkLabel(frame_tabela, text="Análise Léxica e Análise Sintática", font=("Helvetica", 15), text_color="white")
texto_analise_lexica.pack(side="top", fill="y", padx=10, pady=(0, 0))

# Adicionar a tabela (Treeview) no frame
columns = ("token", "lexema", "palavra_reservada")
style = ttk.Style()

style.theme_use("default")

# Configurar cores para o Treeview
style.configure("Treeview",
                background="#2a2d2e",
                foreground="white", 
                rowheight=18,
                fieldbackground="#2a2d2e",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])

# Configurar cores para o cabeçalho do Treeview
style.configure("Treeview.Heading",
                background="#565b5e",
                foreground="white",
                relief="flat")
style.map("Treeview.Heading",
          background=[('active', '#22559b')])
tabela_treeview = ttk.Treeview(frame_tabela, columns=columns, show="headings", )
tabela_treeview.pack(side="left", fill="both", expand=True)
tabela_treeview.heading("token", text="TOKENS")
tabela_treeview.heading("lexema", text="LEXEMA")
tabela_treeview.heading("palavra_reservada", text="PALAVRA RESERVADA")

# Criar um estilo para a barra de rolagem vertical
style.configure("Custom.Vertical.TScrollbar",
                background="#242424",  # Altere para a cor desejada
                troughcolor="#343638",  # Altere para a cor desejada
                gripcount=0)  # Esconda a alça de rolagem

# Adicionar uma barra de rolagem vertical ao frame_tabela
vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tabela_treeview.yview)
vsb.pack(side="right", fill="y")

# Configurar a tabela_treeview para usar a barra de rolagem vertical
tabela_treeview.configure(yscrollcommand=vsb.set)

# Adicionar um frame para os botões
button_frame = ctk.CTkFrame(root, fg_color="#242424", bg_color="#242424")
button_frame.grid(row=3, column=0, columnspan=2, pady=(15, 15))

# Adicionar os botões dentro do frame
transpilador_btn = ctk.CTkButton(button_frame, text="Transpilar", command=transpilar)
transpilador_btn.pack(side="left", padx=2)

limpar_btn = ctk.CTkButton(button_frame, text="Limpar", command=limpar)
limpar_btn.pack(side="left", padx=2)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=1)

root.mainloop()