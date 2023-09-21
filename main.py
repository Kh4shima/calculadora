print("Calculadora em Python")
numero1 = int (input("Informe um numero inteiro "))
numero2 = int (input("Informe outro numero inteiro "))
operacao = input("Informe a operação (+ - * /) ")

if operacao == "+":
    print("Resultado: ", numero1 + numero2)
if operacao == "-":
    print("Resultado: ", numero1 - numero2)
if operacao == "*":
    print("Resultado: ", numero1 * numero2)
if operacao == "/":
    print("Resultado: ", numero1 / numero2)
    