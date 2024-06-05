# A3_TCC_Kepler

## Introdução

No desenvolvimento de software, a tradução de código-fonte escrito em linguagens de alto nível para formas executáveis é uma etapa fundamental. Dois processos principais são usados para essa tradução: a compilação e a transpilação.

Um compilador é uma ferramenta que traduz código fonte de uma linguagem de programação de alto nível para código de máquina executável por um computador. Já os transpiladores traduzem código de uma linguagem de programação de alto nível para outra linguagem de programação de alto nível. O objetivo principal de um transpilador é permitir que o código fonte escrito em uma linguagem seja convertido para outra, mantendo o mesmo nível de abstração e legibilidade.

Os processos comuns aos compiladores e transpiladores são:

1. Análise Léxica: Divide o código em tokens.
2. Análise Sintática: Organiza tokens em uma árvore sintática, verificando a estrutura gramatical.
3. Análise Semântica: Assegura a validade semântica do código.

Para concluir a compilação é necessário os seguintes passos: 

4. Otimização: Melhora a eficiência do código intermediário.
5. Geração de Código: Transforma o código intermediário em código de máquina.
6. Montagem e Linkagem: Converte o código de máquina em binário e liga a bibliotecas necessárias.

Enquanto para concluir a transpilação é preciso: 

4. Transformação de Código: Transforma a árvore de sintaxe abstrata para refletir as construções da linguagem alvo.
5. Geração de Código: O código transformado é gerado na linguagem de destino.

Compiladores também podem incluir ferramentas de depuração e análise estática de código. A construção de compiladores é uma área complexa que envolve teoria de linguagens, algoritmos, arquitetura de computadores e otimização de software.

## O que é o trabalho?

O projeto consiste em criar um transpilador da linguagem Kepler para a linguagem Python. Ele aceita que você escreva o código ou submeta um arquivo com o código na linguagem desenvolvida e como saída mostra o código equivalente em Python e dá a opção de gerar um arquivo nesse linguagem.

## Como rodar esse projeto?

### Pré-requisitos
Existem alguns pré-requisitos para rodar esse projeto: 
  1. É preciso ter o python instalado, para instalar o python conforme seu sistema operacional acesse: [Python Download](https://www.python.org/downloads/)
  2. Também é preciso instalar as bibliotecas: [Ply](https://pypi.org/project/ply/), [Custom Tkinter](https://pypi.org/project/customtkinter/0.3/), [Tkinter](https://docs.python.org/pt-br/3/library/tkinter.html)

Após todas as dependências terem sidos corretamente instaladas você deverá rodar o script: 

```
python main.py
```

### Interface

Para melhor visualização do código e da transpilação foi criada uma interface com o customtkinter.


<img src="imagens/Captura de Tela 2024-06-04 às 20.17.21.png" alt="Interface">


1. Botão "Abrir": Permite que carregue um arquivo txt com o código em linguagem kepler.
2. Botão "Transpilar": Ao clicar nesse botão o código na linguagem kepler é transpilado para linguagem python.
3. Botão "Limpar": Limpa as coluna "Código Fonte" e "Código Transpilado".
4. Botão "Salvar": Salva um arquivo com o código equivalente transpilado em python.

## Linguagem Kepler

| TOKENS |  LEXEMAS | EXP REGULAR | DESCRIÇÃO | CORRELAÇÃO NO PYTHON
| -----  | -------- | ----------- | --------- | ---------------------
| KIF | KIF | KIF | Palavra reservada KIF | if
| KELSE | KELSE | KELSE | Palavra reservada KELSE | else
| KWHILE | KWHILE | KWHILE | Palavra reservada KWHILE | while
| KOR | KOR | KOR | Palavra reservada KOR | for
| KRINT | KRINT | KRINT | Palavra reservada KRINT | print
| KINPUT | KINPUT | KINPUT | Palavra reservada KINPUT | input
| KRANGE | KRANGE | KRANGE | Palavra reservada KRANGE | range
| KIN | KIN | KIN | Palavra reservada KIN | in
| KT | KT | KT | Palavra reservada KT | True
| KF | KF | KF | Palavra reservada KF | False
| INTEIRO | 0,1,2,3,4,5,6,7,8,9 | `\d+` | Digito numérico inteiro | int
| DOUBLE | 0,009...9,999 | `([0-9]+\.[0-9]+)\|([0-9]+\.[0-9]+)` | Digito numérico real | float
| STRING | a,b,c...x,y,z | `("[^"]*")` | Caracteres | str
| INT | INT | `INT` | Converte para números inteiros | int()
| VARIAVEL | char(string,inteiro, double)* | `[a-z][a-z_0-9]*` | Declaração de variável | variável
| BOOLEANO | (KT\|KF) | `KT\|KF` | Operador booleano | bool
| OP_MAT_ADICAO | \_mais\_ | \_mais\_ | Operador matemático mais | +
| OP_MAT_SUB | \_menos\_ | \_menos\_ | Operador matemático menos | -
| OP_MAT_MULT | \_vezes\_| \_vezes\_ | Operador matemático multiplicação | *
| OP_MAT_POT | \_elevado\_ | \_elevado\_ | Operador matemático potenciação | **
| OP_MAT_DIV | \_dividido\_ | \_dividido\_ | Operador matemático divisão | /
| OP_EXEC_VIRGULA | , | , | Operador vírgula | ,
| OP_ATRIB_IGUAL | \_recebe\_ | \_recebe\_ | Operador atribuição igual | =
| OP_ATRIB_MAIS_IGUAL | \_mais\_igual\_ | \_mais\_igual\_ | Operador atribuição mais igual (adicionar) | +=
| OP_REL_DUPLO_IGUAL | \_igual\_ | \_igual\_ | Operador relacional duplo igual (comparar se é igual) | ==
| OP_REL_MENOR | \_menor\_ | \_menor\_ | Operador relacional menor | <
| OP_REL_MAIOR | \_maior\_ | \_maior\_ | Operador relacional maior | >
| OP_FINAL_LINHA_CIFRAO | $ | $ | Operador cifrão para indicar final de linha | 
| OP_PRIO_ABRE_PARENTESES | ( | ( | Operador de prioridades abre parênteses | (
| OP_PRIO_FECHA_PARENTESES | ) | ) | Operador de prioridades fecha parênteses | )
| OP_PRIO_ABRE_CHAVES | { | { | Operador de prioridades abre chaves | {
| OP_PRIO_FECHA_CHAVES | } | } | Operador de prioridades fecha chaves | }


## Explicação do codigo

Importação de Módulos
```python
import ply.lex as lex
from ply import yacc
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

```
Essas linhas importam bibliotecas necessárias para a execução do programa. ply.lex e ply.yacc são usados para análise léxica e sintática. customtkinter e tkinter são usados para criar a interface gráfica.

Análise Léxica
```python
reserved = {
   'KIF'    : 'KIF',
   'KELSE'  : 'KELSE',
   'KWHILE' : 'KWHILE',
   'KOR'    : 'KOR',
   'KRINT'  : 'KRINT',
   'KINPUT' : 'KINPUT',
   'KRANGE' : 'KRANGE',
   'KIN'    : 'KIN',
   'KT'     : 'KT',
   'KF'     : 'KF',
}

tokens = [
    'INTEIRO',
    'DOUBLE',
    'STRING',
    'INT',
    'VARIAVEL',
    'BOOLEANO',
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
    'OP_FINAL_LINHA_CIFRAO', 
    'OP_PRIO_ABRE_PARENTESES',
    'OP_PRIO_FECHA_PARENTESES',
    'OP_PRIO_ABRE_CHAVES',
    'OP_PRIO_FECHA_CHAVES',
] + list(reserved.values())

```
Define palavras reservadas e tokens utilizados no processo de análise léxica. Tokens são elementos básicos da linguagem, como inteiros, strings, operadores e palavras-chave.

Regras de Expressão Regular para Tokens Simples
```python
t_KWHILE = r'KWHILE'
t_KIF    = r'KIF'
t_KELSE  = r'KELSE'
t_KOR    = r'KOR'
t_KRINT  = r'KRINT'
t_KINPUT = r'KINPUT'
t_KIN    = r'KIN'
t_KRANGE = r'KRANGE'
t_KT     = r'KT'
t_KF     = r'KF'
t_OP_MAT_ADICAO            = r'\_mais\_'
t_OP_MAT_SUB               = r'\_menos\_'
t_OP_MAT_MULT              = r'\_vezes\_'
t_OP_MAT_POT               = r'\_elevado\_'
t_OP_MAT_DIV               = r'\_dividido\_'
t_OP_FINAL_LINHA_CIFRAO    = r'\$'
t_OP_EXEC_VIRGULA          = r'\,'
t_OP_ATRIB_IGUAL           = r'\_recebe\_'
t_OP_ATRIB_MAIS_IGUAL      = r'\_mais\_igual\_'
t_OP_REL_DUPLO_IGUAL       = r'\_igual\_'
t_OP_REL_MENOR             = r'\_menor\_'
t_OP_REL_MAIOR             = r'\_maior\_'
t_OP_PRIO_ABRE_PARENTESES  = r'\('
t_OP_PRIO_FECHA_PARENTESES = r'\)'
t_OP_PRIO_ABRE_CHAVES      = r'\{'
t_OP_PRIO_FECHA_CHAVES     = r'\}'

t_ignore = ' \t'  # Ignora espaço e tabulação

```
Essas são definições de expressões regulares que identificam padrões específicos na entrada, representando tokens da linguagem.

Regras de Expressão Regular para Tokens Mais Complexos
```python
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

def t_BOOLEANO(t):
    r'KT|KF'
    return t

```
Estas funções definem regras de expressão regular para identificar tokens mais complexos, como strings, números inteiros, variáveis e booleanos.

Rastreio de Linhas e Tratamento de Erros
```python
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)

```
Funções para rastrear novas linhas no código e para tratar erros léxicos, adicionando tokens de erro a uma lista e ignorando caracteres inválidos.

Análise Sintática
```python
def p_declaracoes_single(p):
    '''
    declaracoes : declaracao
    '''

```
Define uma regra sintática para uma única declaração. Similarmente, outras funções p_* definem as regras de gramática para a linguagem.

Definição das Precedências dos Operadores
```python
precedence = (
    ('left', 'OP_MAT_ADICAO', 'OP_MAT_SUB'),
    ('left', 'OP_MAT_MULT', 'OP_MAT_DIV','OP_MAT_POT'),
)

```
Define a precedência e a associatividade dos operadores matemáticos para resolver ambiguidade na análise sintática.

Tratamento de Erros Sintáticos
```python
errossintaticos = []
def p_error(p):
    global errossintaticos
    errossintaticos.append(p)
    if p:
        print("ERRO SINTÁTICO: ", p)
        return
    else:
        print("ERRO SINTÁTICO: erro de sintaxe desconhecido")
        return 

```
Função para tratar erros sintáticos, adicionando tokens de erro a uma lista e imprimindo uma mensagem de erro.

Criação do Parser
```python
parser = yacc.yacc()
Constrói o parser a partir das regras definidas.

Funções Auxiliares
python
Copy code
def add_lista_saida(t, notificacao):
    saidas.append(( t.type, t.value, notificacao))

saidas = []

```
Funções para adicionar notificações de tokens à lista de saídas e uma lista para armazenar essas saídas.

Função para Transpilar Código
```python
def transpilar_codigo(codigo):
    lexer.input(codigo)
    tokens = []
    for token in lexer:
        tokens.append(token)
    
    codigo_tokens = " ".join([str(token.value) for token in tokens])
    print("String de tokens:", codigo_tokens)
    
    try:
        ast = parser.parse(codigo_tokens)
        print("Sucesso ao gerar árvore de análise sintática.")

        codigo_transpilado = transpilar_para_python(codigo)

        if len(errossintaticos) == 0:
            print("Código transpilado:")
            print(codigo_transpilado)

        return codigo_transpilado

    except Exception as e:
        print("Erro durante a transpilação:", e)
        return None

```
Função que realiza a análise léxica, a análise sintática e a transpilação do código de entrada para Python.

Função para Transpilar Código para Python
```python
def transpilar_para_python(codigo_fonte):
    # Substituições para transpilar para Python
    codigo_fonte = codigo_fonte.replace('_mais_', '+')
    codigo_fonte = codigo_fonte.replace('_menos_', '-')
    codigo_fonte = codigo_fonte.replace('_vezes_', '*')
    codigo_fonte = codigo_fonte.replace('_elevado_', '**')
    codigo_fonte = codigo_fonte.replace('_dividido_', '/')
    codigo_fonte = codigo_fonte.replace('_recebe_', '=')
    codigo_fonte = codigo_fonte.replace('_mais_igual_', '+=')
    codigo_fonte = codigo_fonte.replace('_igual_', '==')
    codigo_fonte = codigo_fonte.replace('_menor_', '<')
    codigo_fonte = codigo_fonte.replace('_maior_', '>')
    codigo_fonte = codigo_fonte.replace('$', '')
    codigo_fonte = codigo_fonte.replace('KOR', 'for')
    codigo_fonte = codigo_fonte.replace('KELSE', 'else')
    codigo_fonte = codigo_fonte.replace('KINPUT', 'input')
    codigo_fonte = codigo_fonte.replace('KIF', 'if')
    codigo_fonte = codigo_fonte.replace('KRINT', 'print')
    codigo_fonte = codigo_fonte.replace('{', '   ').replace('}', '')
    codigo_fonte = codigo_fonte.replace('KT', 'True')
    codigo_fonte = codigo_fonte.replace('KF', 'False')
    # Correções adicionais
    ...
    return codigo_fonte

```
Esta função substitui as construções da linguagem original pelas equivalentes em Python, realizando a transpilação.

Definição da Interface Gráfica
```python
# Funções para abrir arquivos e iniciar a transpilarção
def abrir_arquivo():
    arquivo_path = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
    if arquivo_path:
        with open(arquivo_path, 'r') as file:
            codigo_fonte = file.read()
            return codigo_fonte
    return None

def iniciar_transpilacao():
    codigo_fonte = abrir_arquivo()
    if codigo_fonte:
        codigo_transpilado = transpilar_codigo(codigo_fonte)
        if codigo_transpilado:
            exibir_codigo_transpilado(codigo_transpilado)
        else:
            exibir_mensagem("Erro na transpilação. Verifique o código-fonte.")

def exibir_codigo_transpilado(codigo_transpilado):
    texto_transpilado.delete('1.0', END)
    texto_transpilado.insert(END, codigo_transpilado)

def exibir_mensagem(mensagem):
    texto_transpilado.delete('1.0', END)
    texto_transpilado.insert(END, mensagem)

# Configuração da interface gráfica
root = ctk.CTk()
root.title("Transpilador de Código")
root.geometry("800x600")

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(frame, text="Transpilador")
label.pack(pady=12, padx=10)

botao_abrir = ctk.CTkButton(frame, text="Abrir Arquivo", command=iniciar_transpilacao)
botao_abrir.pack(pady=12, padx=10)

texto_transpilado = Text(frame, wrap=WORD)
texto_transpilado.pack(pady=12, padx=10, fill="both", expand=True)

root.mainloop()

```
Essas funções configuram a interface gráfica, permitindo ao usuário abrir um arquivo, iniciar a transpilação e exibir o código transpilado.



## Alguns exemplos

### Exemplo de sucesso
#### Entrada: 
```
a _recebe_ 10$
b _recebe_ 20$
KIF a _maior_ b
{ KRINT("A > B")$ }
KELSE
{ KRINT("A < B")$ }
```
#### Saída em Python:
```
a = 10
b = 20

if a > b: 
    print("A > B")
else: 
    print("A < B")
```

<img src="imagens/exemplo1.webp" alt="Exemplo">

### Exemplo de erro
#### Entrada: 
```
a _recebe_ 10$
b _recebe_ 20$
KIF a _maior_ b
{ KRINT("A > B"); }
KELSE
{ KRINT("A < B")$ }
```
#### Saída:
```
O código não está de acordo com as regras da nossa linguagem,
```

<img src="imagens/exemploErro2.webp" alt="Exemplo de Erro">

## Participantes

| Nome                                   | RA          | 
|----------------------------------------|-------------|
| Gabriel Antonio Lopes de Castro        | 1272023100  |  
| Julio Correa De Sagebin Cahú Rodrigues | 1272415912  |  
| João Amaral Lantyer                    | 1271919682  | 
| Marina Fernandes Porto Leite           | 1272121593  | 
| Manoel Felipe Costa Almeida Fernandes  | 12720110473 | 
