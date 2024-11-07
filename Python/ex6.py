print("Calculadora de nota")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

soma = n1 + n2 + n3 + n4

n5 = soma / 4

if n5 == 10:
    print(f"Sua nota final é {n5}, passou com exelencia")
elif n5 >= 7:
    print(f"Sua nota final é {n5}, muito bem")
elif n5 >= 6:
    print(f"Sua nota final é {n5}, Passou por pouco")
else:
    print(f"Sua nota final é {n5}, reprovado")