# nomes_alunos = ["Giovanna", "Gustavo", "Vinicius"]
#
# for nome in nomes_alunos:
#     print(nome)

# nomes_alunos = ["Giovanna", "Gustavo", "Vinicius", "Davi"]
# pesquisa = input("Digite o nome do aluno: ").capitalize()
#
# x = 0
# for nome in nomes_alunos:
#     if nome == pesquisa:
#         print("Nome encontrado.")
#         print(x)
#         break
#     x += 1
#
# else:
#     print("Nome não encontrado.")

# numeros_pares = []
# for num in range(2,11,2):
#     numeros_pares.append(num)
#
# print(numeros_pares)

# notas = [8, 5.5, 7.8, 9.6, 10, 6.2]
# maxima = notas[0]
#
# contador = 0
# for i, nota in enumerate(notas):
#     if nota > maxima:
#         maxima = nota
#         posicao = i
#
# print(posicao)
# print(maxima)

notas = [8, 5.5, 7.8, 9.6, 10, 6.2]
maxima = notas[0]
posicao = 0

contador = 0
for nota in notas:
    if nota > maxima:
        maxima = nota
        posicao = contador
    contador += 1

print(posicao)
print(maxima)