#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 3 - Fazer um dicionário e adicionar 3 disciplinas com sua respectiva nota (ex: {'algoritmos': 90, 'física': 80,
# 'matemática': 70}), depois criar uma estrutura que encontre dentro do dicionário qual foi a menor nota.

#
# entrada de dados
# dicionário d1 - dicionário com valores inteiros
d1 = {'algoritmos':80 , 'Fisica':90, 'matematica':70}

''' 
min (iterável, * [, padrão = obj, chave = func]) -> valor
min (arg1, arg2, * args, * [, chave = func]) -> valor

Com um único argumento iterável, retorna seu menor item. o
argumento padrão apenas de palavra-chave especifica um objeto a ser retornado se
o iterável fornecido está vazio.
Com dois ou mais argumentos, retorna o menor argumento '''


maior = max(d1, key=d1.get)
menor = min(d1, key=d1.get)

print(f'A maior nota é {maior} e a menor nota é {menor}')
