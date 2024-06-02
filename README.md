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

O projeto consiste em criar um transpilador da linguagem que desenvolvemos para a linguagem Python. Ele aceita que você escreva o código ou submeta um arquivo com o código na linguagem desenvolvida e como saída mostra o código equivalente em Python e dá a opção de gerar um arquivo nesse linguagem.

## Como rodar esse projeto?

### Pré-requisitos
Existem alguns pré-requisitos para rodar esse projeto: 
  1. É preciso ter o python instalado, para instalar o python conforme seu sistema operacional acesse: [Python Download](https://www.python.org/downloads/)
  2. Também é preciso instalar as bibliotecas: [Ply](https://pypi.org/project/ply/), [Custom Tkinter](https://pypi.org/project/customtkinter/0.3/), [Tkinter]()

Após todas as dependências terem sidos corretamente instaladas você deverá rodar o script: 

```
exemplo
```

## Linguagem Kepler

| TOKENS |  LEXEMAS | EXP REGULAR | DESCRIÇÃO
| -----  | -------- | ----------- | ---------
| KIF | KIF | KIF | Palavra reservada KIF
| KELSE | KELSE | KELSE | Palavra reservada KELSE
| KWHILE | KWHILE | KWHILE | Palavra reservada KELSE
| KOR | KOR | KOR | Palavra reservada KELSE
| KRINT | KRINT | KRINT | Palavra reservada KELSE
| KINPUT | KINPUT | KINPUT | Palavra reservada KELSE
| KRANGE | KRANGE | KRANGE | Palavra reservada KELSE
| KIN | KIN | KIN | Palavra reservada KELSE
| KT | KT | KT | Palavra reservada KELSE
| KF | KF | KF | Palavra reservada KELSE
| INTEIRO | 0,1,2,3,4,5,6,7,8,9 | `\d+` | Digito numérico inteiro
| DOUBLE | 0,009...9,999 | `([0-9]+\.[0-9]+)\|([0-9]+\.[0-9]+)` | Digito numérico reais
| STRING | a,b,c...x,y,z | `("[^"]*")` | Caracteres
| INT | INT 
| VARIAVEL | char(string,inteiro, double)* | `[a-z][a-z_0-9]*`
| BOOLEANO | (KT\|KF) | `KT\|KF`
| OP_MAT_ADICAO | + | + | Operador matemático mais
| OP_MAT_SUB | - | - | Operador matemático menos
| OP_MAT_MULT | * | * | Operador matemático multiplicação
| OP_MAT_POT | ** | ** | Operador matemático potencição
| OP_MAT_DIV | / | / | Operador matemático divisão
| OP_EXEC_VIRGULA | , | , | Operador virgula
| OP_ATRIB_IGUAL | = | = | Operador atribuição igual 
| OP_ATRIB_MAIS_IGUAL | += | += | Operador atribuição mais igual (adicionar)
| OP_REL_DUPLO_IGUAL | == | == | Operador relacional duplo igual (comparar se é igual)
| OP_REL_MENOR | < | < | Operador relacional menor
| OP_REL_MAIOR | > | > | Operador relacional maior
| OP_FINAL_LINHA_CIFRAO | $ | $ | Operador cifrão para indicar final de linha
| OP_PRIO_ABRE_PARENTESES | ( | ( | Operador de prioridades abre parenteses
| OP_PRIO_FECHA_PARENTESES | ) | ) |  Operador de prioridades fecha parenteses
| OP_PRIO_ABRE_CHAVES | { | { | Operador de prioridades abre chaves
| OP_PRIO_FECHA_CHAVES | } | } | Operador de prioridades fecha chaves


## Explicação do codigo


## Alguns exemplos

#### Entrada: 
```
{
KRINT("Hello World")$
}
```
#### Saída em Python:
```
print("Hello, World!")
```
#### Entrada: 
```
x = 10$
{
KRINT("O valor de x é: ", x)$
}
```
#### Saída em Python:
```
x = 10
print("O valor de x é: ", x)
```

## Participantes

| Nome                                   | RA          | 
|----------------------------------------|-------------|
| Gabriel Antonio Lopes de Castro        | 1272023100  |  
| Julio Correa De Sagebin Cahú Rodrigues | 1272415912  |  
| João Amaral Lantyer                    | 1271919682  | 
| Marina Fernandes Porto Leite           | 1272121593  | 
| Manoel Felipe Costa Almeida Fernandes  | 12720110473 | 
