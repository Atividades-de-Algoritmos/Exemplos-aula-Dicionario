#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 1 - verificar se um determinado valor existe em um dicionário.
# #Obs: podemos usar o método values(), que retorna os valores como uma lista e, em seguida, usar o operador in.

# entrada de dados

d1 = {'a': 100, 'b': 200, 'c': 300} # dicionário d1 - dicionário com valores inteiros

######  1  ################
print(200 in d1.values()) # verifica se o valor 200 existe em d1 e retorna um valor booleano (True ou False)

######  2  ################
valor = input("informe um valor: ") # entrada de dados - valor a ser verificado se existe em d1 (inteiro)
print(valor in d1.values()) # retorna False porque esta entrando um STR e não INT como valor a ser verificado se existe em d1

######  3  ################
valor = int(input("informe um valor: ")) # entrada de dados - valor a ser verificado se existe em d1 (inteiro)
print(valor in d1.values()) # retorna True porque esta entrando um INT e não STR como valor a ser verificado se existe em d1
