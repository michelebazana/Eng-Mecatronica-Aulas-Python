# media_final = float(input("Média final de 0 a 10: "))
#
# if media_final >= 6:
#     print("Aprovado!")
# else:
#     print("Reprovado!")

# Exercício 1
# velocidade = float(input("Velocidade do carro: "))
# if velocidade > 80:
#     print("Você foi multado!")
#     multa = (velocidade - 80) * 5
#     print(f"O valor da multa é R$ {multa:.2f}")
# else:
#     print("Parabéns! Você está dentro velocidade permitida!")

# Exercício 2
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"O maior número é {num3}")

if num1 <= num2 and num1 <= num3:
    print(f"O menor número é {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"O menor número é {num2}")
elif num3 <= num1 and num3 <= num2:
    print(f"O menor número é {num3}")

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
# print(maior)
# print(menor)
