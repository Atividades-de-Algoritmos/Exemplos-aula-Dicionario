#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 30/07/2022
#
# Exercício 2: Obtenha a chave de um valor mínimo do seguinte dicionário;
# d1 = {'Física': 82, Matemática': 65, 'História': 75}

# -- Entrada de dados --

notas = {
  'Física': 82,
  'Matemática': 65, # Dicionário d1 - Dicionário com valores inteiros para cada matéria
  'Historia': 75
  }

# -- Processamento de dados --

# // Com a função min()

menor_nota = min(notas.values()) # Obtendo o valor mínimo do dicionário

# // Sem a função min() Vejam como as funções facilitam nossas vidas xD

for indice, valor in enumerate(notas.values()): # Usei o enumerate para criar uma tupla com os valores e os indíces
  if indice == 0: # Quero que quando for o início ele defina o primeiro valor como a menor nota
    menor_nota = valor # Definindo a menor nota como o primeiro valor do dicionário

  if valor < menor_nota: # Se o novo valor do dicinário for menor que o anterior, o novo valor deve se tornar a menor nota
    menor_nota = valor # Definindo a menor nota como um novo valor.
  
  else: # Se não, vai executar o pass e segue percorrendo o dicionário até os elementos chegarem ao fim.
    pass # Ignora um ciclo de código, e passa uma linha.

# -- Saída de dados --

print(f'Dicionário: {notas}')
print(f'\nMenor valor: {menor_nota}') # Imprimindo o valor mínimo do dicionário
print("\nFim do programa") # Imprimindo ao usuário que o programa terminou
