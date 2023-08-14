print("Bem Vindo a minha primeira calculadora :)")
def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a, b):
    return a * b

def div(a,b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

escolha = input("O que você deseja fazer? +, -, /, ou * : ")

if escolha in ("+", "-", "/", "*"):
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    if escolha == '+':
        print("Resultado:", soma(n1, n2))
    elif escolha == '-':
        print("Resultado:", sub(n1, n2))
    elif escolha == '*':
        print("Resultado:", mult(n1, n2))
    elif escolha == '/':
        print("Resultado:", div(n1, n2))
else:
    print("Escolha inválida")