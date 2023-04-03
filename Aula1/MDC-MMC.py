#O máximo divisor comum é encontrado quando multiplicamos os fatores que dividem simultaneamente os números fatorados.

numero1  = int(input("Informe o numero da posiçao A: "))
numero2 = int(input("Informe o numero da posiçao B: "))

def mdc(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    while r !=0:
        a = b
        b = r 
        r = a%b
    return b

def mmc(num1, num2):
    a = num1
    b = num2

    resto = None
    while resto !=0:
        resto = a % b
        a = b
        b = resto

    return (num1 * num2) / a


operaçao1 = mmc(numero1, numero2)
operaçao2 = mdc(numero1, numero2)

print(operaçao1)
print(operaçao2)

