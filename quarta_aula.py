# print(1)
# print(2)
# print(3)
# print()
#
# x = 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(f"{x}\n")
#
# x = 1 # contador
# while x <= 3: # condição
#     print(x)
#     #x = x + 1
#     x += 1

# Exercício 3

# from time import sleep
#
# x = 10
# while x >= 0:
#     print(x)
#     sleep(1)
#     x -= 1
#
# print("Fogo!")

# fim = int(input("Digite o nº de parada: "))
# x = 2 # contador
# while x <= fim: # condição
#     print(x)
#     x += 2

# num = int(input("Tabuada de: "))
# x = 1
# while x <= 10:
#     print(f"{num} x {x} = {num * x}")
#     x += 1

# num = int(input("Tabuada de: "))
# inicio = int(input("Início: "))
# fim = int(input("Fim: "))
# while inicio <= fim:
#     print(f"{num} x {inicio} = {num * inicio}")
#     inicio += 1

soma = 0 # acumulador
x = 0 # contador
while x < 3:
    x += 1
    check = float(input(f"Checkpoint {x}: "))
    soma += check

print(f"Média = {soma/x}")


