print("Calculadora")

n1 = int(input("Insira 1 numero: "))
n2 = int(input("Insira 1 numero: "))

print("equações")
print("1 = soma")
print("2 = subtração")
print("3 = multiplicação")
print("4 = divisão")

eq = int(input("Escolha a Equação: "))

if eq == 1:
    print(f"A soma de {n1} + {n2} = {n1+n2}")
elif eq == 2:
    print(f"A sutração de {n1} - {n2} = {n1-n2}")
elif eq == 3:
    print(f"A multiplicação de {n1} x {n2} = {n1*n2}")
elif eq == 4:
    print(f"A divisão de {n1} / {n2} = {n1/n2}")
else:
    print("Numero não valido")