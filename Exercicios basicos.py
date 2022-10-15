# Exercicio 1
numero = int(input("Digite um numero:"))
numero2 = int(input("Digite outro numero:"))
print("A soma do numero {} + {} é igual:{}".format(numero, numero2, (numero + numero2)))

# Exercicio 2

dado1 = int(input("A:Digite um numero:"))
dado2 = int(input("B:Digite outro numero:"))
dado3 = int(input("C:Digite mais um numero:"))

if dado1 >= dado2 and dado1 >= dado3:
    print("A é o maior numero:", dado1)
elif dado2 >= dado3:
    print("B é o maior numero:", dado2)
else:
    print("C é o maior numero:", dado3, "\n")

# Exercicio 3

number1 = int(input("A:Digite um numero:"))
number2 = int(input("B:Digite outro numero:"))
number3 = int(input("C:Digite mais um numero:"))

if number1 <= number2 and number1 <= number3:
    print("A é o menor numero:", number1)
elif number2 <= number3:
    print("B é o menor numero:", number2)
else:
    print("C é o menor numero:", number3, "\n")

# exercicio 4

radiacao = int(input("Qual o nivel da radiação:"))
if radiacao <= 9:
    print("Situação Normal")
else:
    print("Situação Grave")
if radiacao >= 11:
    print("Erro")
else:
    print("Está entre 0 e 10")
if radiacao <= 0o3:
    print("Baixo")

# Exercicio 5

# 3lados
# 2lados
# ladosdifirentes

lado = float(input("Digite um numero:"))
lado1 = float(input("Digite outro numero:"))
lado2 = float(input("Digite mas um numero:"))

if not (lado + lado1 > lado2 and lado + lado2 > lado1 and lado1 + lado2 > lado):
    print("Não é um triangulo")
elif lado == lado1 and lado1 == lado2:
    print("È um Equilatero")
elif lado == lado1 or lado == lado2 or lado1 == lado2:
    print("Isoceles")
else:
    print("Escaleno")
