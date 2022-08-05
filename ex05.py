#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 30/07/2022
#
# 5 - Crie um dicionário para armazenar o nome do aluno (chave) e 4 notas (elementos) para 3 alunos.
# Faça uma estrutura de repetição para pedir os valores
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média. Ex;
#
# d1  = {
#         aluno1: notas[],
#         aluno2: notas[],
#         aluno3: notas[]
#       }

# -- Entrada de dados --

alunos = {} # Criando um dicionário vazio para armazenar os nomes e as notas dos alunos

for i in range(1, 4): # Estrutura de repetição python, começa do 1 e vai até o 3 parando no 4
    print() # Print() vazio apenas para deixar uma linha no console
    nome = input(f"Informe o nome do aluno[{i}]: ") # Solicitando o nome do aluno do usuário
    notas = list() # Criando uma lista vazia para armazenar as notas do aluno
    print() # Print() vazio apenas para deixar uma linha no console
    
    for y in range(1, 5): # Estrutura de repetição python, começa do 1 e vai até o 4 parando no 5
        notas.append(int(input(f"informe a nota[{y}] do aluno {nome}: "))) # Solicitando e adicionando a nota na lista usando a função .append()
    
    alunos[nome] = notas # Adicionando como chave nome do aluno e a lista com as nota como elemento do dicionário


# -- Processamento e saída de dados --

print(f'\nDicionário alunos: {alunos}') # Imprimindo o dicionário alunos

for y in alunos: # Percorrendo as chaves do dicionário alunos
  somaNotas = 0  # Criando uma variável para ser a soma das notas
  
  for i in alunos[y]: # Percorrendo a lista das notas do aluno
    somaNotas += i # Somando as notas do aluno
  
  media = somaNotas / len(alunos) # Calculando a média das notas do aluno
  print(f"\n{y} teve média {media:.1f}") # Imprimindo a o cálculo das da média de cada aluno

  # Outra maneira é utilizando a função sum()
  
  if 'quiser executar a segunda parte' == False: # Travando para que o código de baixo não execute seja só demonstração !!!
    somaNotas = sum(alunos[y]) # Função sum() vai percorrer toda a lista das notas e retornar o valor da soma
    media = somaNotas/len(alunos) # Calculando a média fazendo a soma das notas divido pela quantidade de notas
    print(f"{y} teve média {media}")

print("\nFim do programa")
