#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
#4. #Crie uma estrutura de repetição para fazer a leitura de vários números inteiros e ímpares e os armazene
# dentro de uma lista, quando essa lista chegar a 5 elementos pare com a leitura. Em seguida, converta essa
# lista em uma tupla e crie outra estrutura de repetição para calcular a média entre todos os valores dentro
# da tupla.

lista1 = list() # lista1 - lista vazia

while True: # estrutura de repetição
    num = int(input("informe um número inteiro: ")) # entrada de dados - número inteiro
    if not(num % 2 == 0): # se o número for ímpar então adiciona na lista1
        lista1.append(num)
    if len(lista1) == 5: # se a lista1 tiver 5 elementos então pare com a leitura
        print(lista1) # imprime a lista1 com os 5 elementos que foram adicionados
        break # para o loop

tupla1 = tuple(lista1) # converte a lista1 em uma tupla
print(tupla1) # imprime a tupla1
soma = 0 # soma - inicialização da soma com 0
for i in tupla1: # percorre a tupla1 e soma os valores da tupla1
    soma += i # soma os valores da tupla1

media = soma / len(tupla1) # calcula a média entre os valores da tupla1
print(f"a média foi de {media}") # imprime a média entre os valores da tupla1

# ou

soma = sum(tupla1) # soma os valores da tupla1 com o método sum()
media = soma / len(tupla1) # calcula a média entre os valores da tupla1
print(f"a média foi de {media}") # imprime a média entre os valores da tupla1