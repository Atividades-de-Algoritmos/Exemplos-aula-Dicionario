#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# Exercício 2: obtenha a chave de um valor mínimo do seguinte dicionário
# d1 = {'Física': 82, Matemática': 65, 'História': 75}
# entrada de dados
#

# dicionário d1 - dicionário com valores inteiros
d1 = {
  'Física': 82,
  'Matemática': 65,
  'Historia': 75}

# 1 - verificar se um determinado valor existe em um dicionário.
t = min(d1.values()) # obtém o valor mínimo do dicionário d1
print(t) # imprime o valor mínimo do dicionário d1 (65)

for i in d1: # percorre o dicionário d1 e verifica se o valor mínimo existe em cada chave do dicionário d1
     if (d1[i] == t): # se o valor mínimo existe em cada chave do dicionário d1 então imprime a chave que contém o valor mínimo
         print(i) # imprime a chave que contém o valor mínimo do dicionário d1
         break # para o loop

print("final do programa")