#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 30/07/2022
#
# 1 - Verificar se um determinado valor existe em um dicionário.
# Obs: podemos usar o método values(), que retorna os valores como uma lista e, em seguida, usar o operador in.

# -- Entrada de dados --

d1 = {'a': 100, 'b': 200, 'c': 300} # Dicionário d1 - Dicionário com valores inteiros
print(f'Dicionário d1: {d1}')

# -- Processamento e saída de dados --

# // 1º Forma
valor = int(input('\nInforme um valor inteiro: ')) # Solicitando um valor inteiro do user
print(f'\n{valor in d1.values()}') # Verifica se um valor qualquer existe em d1 e imprime um valor booleano (True ou False)

# // 2º Forma com falha
valor = input("\nInforme um valor: ") # Solictando um valor em str do user
print(f'\n{valor in d1.values()}') # Imprime False porque esta entrando um STR e não INT como valor a ser verificado se existe em d1

print('\nFim do programa')