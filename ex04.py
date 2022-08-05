#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 30/07/2022
#
# 4 - Crie uma estrutura de repetição para fazer a leitura de vários números inteiros e ímpares e os armazene.
# Quando essa lista chegar a 5 elementos pare com a leitura.
# Em seguida, converta essa lista em uma tupla e crie estrutura de repetição para calcular a média entre todos os valores

# -- Entrada e processamento de dados -- 

lista1 = list() # Criando uma lista vazia com o construtor list()

while True: # Criando um looping infinito com While True:
    num = int(input("Informe um número inteiro: ")) # Solicitando um valor inteiro do user
    
    if not(num % 2 == 0): # Se o número for ímpar então adiciona dentro da lista
        lista1.append(num) # Adicionando o valor dentro da lista com o .append()
    
    else: # Se o número não for ímpar, ele continua sendo um inteiro então adicionaremos dentro da lista
        lista1.append(num) # Adicionando o valor dentro da lista com o .append()
    
    if len(lista1) == 5: # Se a lista1 tiver 5 elementos então pare com a leitura
        print(f'\nLista: {lista1}') # Imprimindo a lista1 com os 5 elementos que foram adicionados
        break # Break está quebrando o laço de repetição

# -- Saída de dados --

tupla1 = tuple(lista1) # Convertendo a lista1 em uma tupla
print(f'Tupla: {tupla1}') # Imprimindo a tupla1 com os 5 elementos que foram adicionados

soma = 0 # Criando uma variável para armazenar o valor da soma

# // Usando estrutura de repetição para fazer a soma dos valores

for i in tupla1: # Percorre por completo toda a tupla1
    soma += i # Soma todos os valores encontrados na tupla

media = soma / len(tupla1) # Calculando a média, a soma dos valores dividido pela quantidade de elementos
print(f"\nA média foi de: {media}") # Imprimindo a média calculada acima

# // Usando a função sum() para fazer a soma dos valores

soma = sum(tupla1) # Somando os valores da tupla1 com o método sum()
media = soma / len(tupla1) # Calculando a média entre os valores da tupla1