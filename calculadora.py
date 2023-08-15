def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return "no se puede dividir entre 0"
    
print("calculadora")
print("Solo acepta operaciones basicas")

signo = input("ingrese la operacion a realizar(+,-,*,/): ")
num1 = float(input("ingrese primer numero: "))
num2 = float(input("ingrese segundo numero: "))

if signo == "+":
    resultado = sumar(num1,num2)
elif signo == "-":
    resultado = restar(num1,num2)
elif signo == "*":
    resultado = multiplicar(num1,num2)
elif signo == "/":
    resultado = dividir(num1,num2)


print("resultado: ",resultado)