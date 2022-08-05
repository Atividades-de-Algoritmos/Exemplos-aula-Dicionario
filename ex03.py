#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 30/07/2022
#
# 3 - Fazer um dicionário e adicionar 3 disciplinas com sua respectiva nota Ex;
# Disciplinas = {'algoritmos': 90, 'física': 80, 'matemática': 70}, depois usamos as funções max() e min() passando parâmetros get()

# -- Entrada de dados --

notas = {'algoritmos':80 , 'Fisica':90, 'matematica':70} # Dicionário d1 - dicionário com valores inteiros das notas

''' # --- Explicação ---

min (iterável, * [, padrão = obj, chave = func]) -> valor
min (arg1, arg2, * args, * [, chave = func]) -> valor

Com um único argumento iterável, retorna seu menor item. o
argumento padrão apenas de palavra-chave especifica um objeto a ser retornado se
o iterável fornecido está vazio.
Com dois ou mais argumentos, retorna o menor argumento 
--- ---
'''

# -- Processamento de dados --

maior = max(notas, key = notas.get) # A func max() aceita como parâmetros além do iterável uma chave que vai ser uma outra função que irá mudar o iterável, por exemplo, 'notas.get' está passando pra ele iterar os values do dicionario, se fosse len iria se basear no tamanho das chaves do dicionario.

menor = min(notas, key = notas.get) # A func min() aceita como parâmetros além do iterável uma chave que vai ser uma outra função que irá mudar o iterável, por exemplo, 'notas.get' está passando pra ele iterar os values do dicionario, se fosse len iria se basear no tamanho das chaves do dicionario.

# -- Saída de dados --

print(f'A maior nota é da disciplina {maior} e a menor nota é da disciplina {menor}')

print('\nFim do programa')