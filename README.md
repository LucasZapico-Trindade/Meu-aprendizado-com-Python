🐍 Minha Jornada de Aprendizado em Python - Fundamentos
Este repositório documenta minha evolução no aprendizado dos conceitos fundamentais da linguagem Python, desde os primeiros passos até o domínio de funções.
📖 Sobre Esta Jornada
Aqui registro minha progressão sistemática através dos pilares essenciais do Python, com exemplos práticos e anotações sobre cada conceito aprendido.

🗂️ Estrutura do Conhecimento
1.  Introdução e Sintaxe Básica
Primeiro contato com a linguagem

Sintaxe e estrutura básica

Comentários e documentação

Exemplo:

python
# Meu primeiro programa em Python
print("Hello, World!")  # Saída: Hello, World!

# Variáveis simples
nome = "João"
idade = 25
2. 📊 Tipos de Dados e Variáveis
Tipos primitivos (int, float, str, bool)

Declaração e manipulação de variáveis

Conversão entre tipos

Conceitos Praticados:

python
# Diferentes tipos de dados
inteiro = 10
decimal = 3.14
texto = "Python"
booleano = True

# Conversão de tipos
numero_texto = str(inteiro)  # "10"
texto_numero = int("123")    # 123
3. 🔢 Operadores
Operadores aritméticos (+, -, *, /, %, **)

Operadores de comparação (==, !=, >, <)

Operadores lógicos (and, or, not)

Exemplos:

python
# Operadores aritméticos
soma = 5 + 3        # 8
potencia = 2 ** 3   # 8
resto = 10 % 3      # 1

# Operadores lógicos
resultado = (5 > 3) and (2 == 2)  # True
4. 🎮 Estruturas de Controle
Condicionais (if, elif, else)

Loops (for, while)

Controle de fluxo (break, continue)

Condicionais:

python
# Estrutura if/elif/else
idade = 18

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
Loops:

python
# Loop for
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop while
contador = 0
while contador < 3:
    print(contador)
    contador += 1
5. 🗃️ Estruturas de Dados Básicas
Listas

Tuplas

Dicionários

Sets

Listas:

python
# Criando e manipulando listas
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")          # Adiciona item
frutas.remove("banana")       # Remove item
primeira_fruta = frutas[0]    # Acessa por índice
Dicionários:

python
# Trabalhando com dicionários
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores
print(pessoa["nome"])    # Maria
print(pessoa.get("idade")) # 30

6. 📝 Funções
Definição e chamada de funções
Parâmetros e argumentos
Retorno de valores
Escopo de variáveis
Funções Básicas:

python
# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Ana")
print(mensagem)  # Olá, Ana!
Funções com Múltiplos Parâmetros:

python
# Função com parâmetros e retorno
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC)
    
    Args:
        peso (float): Peso em kg
        altura (float): Altura em metros
    
    Returns:
        float: Valor do IMC
    """
    return peso / (altura ** 2)

# Usando a função
imc = calcular_imc(70, 1.75)
print(f"IMC: {imc:.2f}")
Funções com Valores Padrão:

python
# Parâmetros com valores default
def cumprimentar(nome, mensagem="Olá"):
    return f"{mensagem}, {nome}!"

print(cumprimentar("Carlos"))           # Olá, Carlos!
print(cumprimentar("Ana", "Bom dia"))   # Bom dia, Ana!

Exercícios Práticos
Desafios Resolvidos
Calculadora Básica - Operações matemáticas fundamentais
Verificador de Números - Par/Ímpar, Positivo/Negativo
Contador de Palavras - Manipulação de strings
Gerenciador de Listas - Operações com listas
Conversor de Unidades - Reutilização de funções

Meu Progresso
Conceitos Dominados
Sintaxe básica e indentação
Variáveis e tipos de dados
Operadores (aritméticos, comparativos, lógicos)
Estruturas condicionais (if/elif/else)
Loops (for, while)
Estruturas de dados (listas, dicionários, tuplas)
Funções (definição, parâmetros, retorno)

🔄 Próximos Passos
Programação Orientada a Objetos
Tratamento de exceções
Módulos e pacotes
Manipulação de arquivos

Principais Aprendizados
Insights Importantes
Indentação é crucial em Python - define blocos de código
Tipagem dinâmica facilita o desenvolvimento
List comprehensions tornam o código mais pythonico
Funções melhoram a organização e reutilização do código

Desafios Superados
Ajustar à sintaxe baseada em indentação
Compreender o escopo de variáveis em funções
Diferenciar entre métodos que modificam vs. retornam cópias
Esteb repositório é um diário vivo do meu aprendizado. Volte sempre para acompanhar minha evolução! 🐍✨
