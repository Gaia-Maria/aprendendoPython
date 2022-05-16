#
# Arquivo com exemplos de funções
#

# definindo uma função básica
def func1():
    print("Eu sou uma função")

func1()    

# função que recebe argumentos
def func2(arg1, arg2):
    print(arg1 + " " + arg2)

func2("Gaia" , "Maria")

# função que retorna um valor
def cubo(x):
    return x* x* x

f = cubo(7)
print(f)
print(cubo(9))

# teste
def func3(pessoa1, pessoa2, pessoa3):
    print(pessoa1 + " " + pessoa2 + " " + pessoa3)

func3("isabela", "bruna", "camila")

# teste2
def numero(y):
    return y* y* y

f = numero(9)
print(f)
