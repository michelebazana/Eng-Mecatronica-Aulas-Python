# media_final = float(input("Média final = "))
# if media_final >= 6:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Exercício 1
# vel = int(input("Velocidade em km = "))
# if vel > 80:
#     print("Você foi multado.")
#     multa = (vel - 80) * 5
#     print(f"O valor da multa é R${multa:.2f}")
# else:
#     print("Você não foi multado")

# Exercício 2
# num1 = float(input("Número 1 = "))
# num2 = float(input("Número 2 = "))
# num3 = float(input("Número 3 = "))
#
# maior = num1
# if num2 >= num1 and num2 >= num3:
#     maior = num2
# if num3 >= num1 and num3 >= num2:
#     maior = num3
#
# menor = num1
# if num2 <= num1 and num2 <= num3:
#     menor = num2
# if num3 <= num1 and num3 <= num2:
#     menor = num3
#
# print(f"O número maior é {maior}")
# print(f"O número menor é {menor}")

# Exercício 3
# sal = float(input("Salário = R$ "))
# if sal > 1250:
#     aumento = sal * 0.1
# else:
#     aumento = sal * 0.15
#     print(aumento)
# print(f"O aumento é de R${aumento:.2f}")

# Exercício 4
dis = int(input("Distância em km = "))
if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45
print(f"O valor da passagem é R${preco:.2f}")
