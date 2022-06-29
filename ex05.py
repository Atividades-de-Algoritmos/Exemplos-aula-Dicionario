#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
  #5 - Crie um dicionário para armazenar o nome do aluno (chave) e 4 notas (elementos) para 3 alunos,
# fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura
# de repetição para somar todas as notas e retornar a média.
# {aluno: notas}
# {aluno1: notas, aluno2: notas, aluno3: notas}
# {aluno1: notas[], aluno2: notas[], aluno3: notas[]}
#
# criar um dicionário para armazenar o nome do aluno (chave) e 4 notas (elementos) para 3 alunos
alunos = {} # alunos - dicionário vazio para armazenar o nome do aluno (chave) e 4 notas (elementos) para 3 alunos

for _ in range(1,4): # estrutura de repetição - 1 a 3
    nome = input(f"informe o nome do aluno[{_}]: ") # entrada de dados - nome do aluno
    notas = list() # notas - lista vazia para armazenar as notas do aluno
    for _ in range(4): # estrutura de repetição - 1 a 4
        notas.append(int(input(f"informe a nota[{_+1}] do aluno {nome}: "))) # entrada de dados - nota do aluno
    alunos[nome] = notas # adiciona o nome do aluno e as notas na chave do dicionário alunos

print(alunos) # imprime o dicionário alunos

for _ in alunos: # estrutura de repetição - 1 a 3
  #alunos[_] - chave do dicionário alunos
  somaNotas = 0  # somaNotas - inicialização da soma das notas com 0
  for i in alunos[_]:
    somaNotas += i # somaNotas + nota do aluno
  media = somaNotas/len(alunos) # calcula a média das notas do aluno
  print(f"{_} teve média {media}")

  # ou
  # somaNotas = sum(alunos[_]) # somaNotas = soma das notas do aluno
  # media = somaNotas/len(alunos) # calcula a média das notas do aluno
  # print(f"{_} teve média {media}")
  print("fim do programa")