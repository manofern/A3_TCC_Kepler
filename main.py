import ply.lex as lex
from ply import yacc
from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog as fd

#Análise Léxica
                                               # Palavras Reservadas do Compilador
reserved = {
   'KIF' : 'KIF',
   'KELIF' : 'KELIF',
   'KELSE' : 'KELSE',
   'KWHILE' : 'KWHILE',
   'KOR':'KOR',
   'KT':'KT',
   'KF':'KF',
   'KRINT':'KRINT',
   'KINPUT':'KINPUT',
}

# Lista para os nomes dos tokens. Esta parte é sempre Requerida pela Biblioteca PLY
tokens = [
                                                     #Operadores Matemáticos
'OP_MAT_MAIS' ,        #+
'OP_MAT_MENOS' ,       #-
'OP_MAT_VEZES',        #*
'OP_MAT_DIVIDE',       #/
'OP_MAT_MODULO',       #%
                                                    #Operadores de Execução
'OP_EXEC_DOIS_PONTOS' ,         #:
'OP_EXEC_PONTO_VIRGULA',        #;
'OP_EXEC_VIRGULA',              #,
'OP_EXEC_PONTO',                #.
                                                    #Operadores de Impressão
'OP_IMP_ASPAS',    #"
'OP_COMENTARIO',   ##
'OP_FINALLINHA',   #final de linha
                                                    #Operadores de Atribuição
'OP_ATRIB_NEGACAO',          #!
'OP_ATRIB_IGUAL',            #=
'OP_ATRIB_MAIS_IGUAL',       #+=
'OP_ATRIB_MENOS_IGUAL',      #-=
'OP_ATRIB_VEZES_IGUAL',      #*=
'OP_ATRIB_DIVIDE_IGUAL',     #/=
                                                     #Operadores Relacionais
'OP_REL_MENOR',           #<
'OP_REL_MAIOR',           #>
'OP_REL_MENOR_IGUAL',     #<=
'OP_REL_MAIOR_IGUAL',     #>=
'OP_REL_DUPLO_IGUAL',     #==
'OP_REL_DIFERENTE',       #!=
'OP_REL_E',               #&&
'OP_REL_OU' ,             #||
                                                    #Operadores de Prioridade
'OP_PRIO_ABRE_PARENTESES',       #(
'OP_PRIO_FECHA_PARENTESES',      #)
'OP_PRIO_ABRE_COLCHETES',        #[
'OP_PRIO_FECHA_COLCHETES',       #]
'OP_PRIO_ABRE_CHAVES',           #{
'OP_PRIO_FECHA_CHAVES',          #}
                                                    #Identificadores
'INTEIRO',      #inteiro
'DOUBLE',       #double
'STRING',       #string
'CHAR',         #char
'VARIAVEL',     #variavel
'TESTE',

#para a criação dos RegEx (para verificar as compatibilidades) com o PLY,as verificações tem que ter uma "chamada" pelo token, é padrão
'IGNORE',      #Ignorar tabulação e espaço

'variavel_mf', #variavel mal formada
'numero_mf',   #numero mal formado
'string_mf',   #string mal formada

] + list(reserved.values()) #concateno com as palavras reservadas para verificação

#Regras de expressão regular (RegEx) para tokens simples
t_OP_MAT_MAIS    = r'\+'
t_OP_MAT_MENOS   = r'-'
t_OP_MAT_VEZES   = r'\*'
t_OP_MAT_DIVIDE  = r'/'
t_OP_MAT_MODULO = r'\%'

t_OP_EXEC_DOIS_PONTOS = r'\:'
t_OP_EXEC_PONTO_VIRGULA = r'\;'
t_OP_EXEC_VIRGULA = r'\,'
t_OP_EXEC_PONTO = r'\.'

t_OP_IMP_ASPAS = r'\"'
t_OP_COMENTARIO = r'\#.*'

t_KWHILE = r'KWHILE'
t_KIF = r'KIF'
t_KELIF = r'KELIF'
t_KELSE = r'KELSE'

t_KOR = r'KOR'

t_KT = r'KT'
t_KF = r'KF'
t_KRINT = r'KRINT'
t_KINPUT = r'KINPUT'

t_OP_ATRIB_NEGACAO = r'\!'
t_OP_ATRIB_IGUAL = r'\='
t_OP_ATRIB_MAIS_IGUAL = r'\+\='
t_OP_ATRIB_MENOS_IGUAL = r'\-\='
t_OP_ATRIB_VEZES_IGUAL = r'\*\='
t_OP_ATRIB_DIVIDE_IGUAL = r'\/\='

t_OP_REL_MENOR = r'\<'
t_OP_REL_MAIOR= r'\>'
t_OP_REL_MENOR_IGUAL = r'\<\='
t_OP_REL_MAIOR_IGUAL = r'\>\='
t_OP_REL_DUPLO_IGUAL = r'\=\='
t_OP_REL_DIFERENTE = r'\!\='
t_OP_REL_E= r'\&\&'
t_OP_REL_OU = r'\|\|'

t_OP_PRIO_ABRE_PARENTESES  = r'\('
t_OP_PRIO_FECHA_PARENTESES  = r'\)'
t_OP_PRIO_ABRE_COLCHETES = r'\['
t_OP_PRIO_FECHA_COLCHETES = r'\]'
t_OP_PRIO_ABRE_CHAVES = r'\{'
t_OP_PRIO_FECHA_CHAVES = r'\}'

t_ignore  = ' \t' #ignora espaço e tabulação

#Regras de expressão regular (RegEx) para tokens mais "complexos"

def t_STRING(t):
    r'("[^"]*")'
    return t

def t_string_mf(t):
    r'("[^"]*)'
    return t

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
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

#Defina uma regra para que seja possível rastrear o números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_OP_FINALLINHA(t):
    r'\''
    return t
    t.lexer.lineno += len(t.value)

#Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)

# Test it out
data = '''
KIF (KT):
    KRINT("A")
'''

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input(data)

# Tokenize

dict = {
    "KIF": "IF"
    
    }
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(vars(tok))

