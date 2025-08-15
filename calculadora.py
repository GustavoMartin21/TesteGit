def somar (a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Raiz quadrada de número negativo"
    return a ** 0.5

def raiz_cubica(a):
    return a ** (1/3)  

def fatorial(n):
    if n < 0:
        return "Erro: Fatorial de número negativo"
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def porcentagem(total, percentual):
    return (total * percentual) / 100  

def logaritmo(a, base=10):
    import math
    if a <= 0 or base <= 1:
        return "Erro: Logaritmo indefinido para esses valores"
    return math.log(a, base)

def seno(angulo):
    import math
    return math.sin(math.radians(angulo)) 
 
def cosseno(angulo):
    import math
    return math.cos(math.radians(angulo))

def tangente(angulo):
    import math
    return math.tan(math.radians(angulo))

def porcentagem(total, percentual):
    return (total * percentual) / 100

def logaritmo(a, base=10):
    import math
    if a <= 0 or base <= 1:
        return "Erro: Logaritmo indefinido para esses valores"
    return math.log(a, base)