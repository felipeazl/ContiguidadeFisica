#Importar o arquivo contedo as funções.
from Funções import Lista

#Usuario digita o tamnho da lista que ele pretende criar.
tamanho = int(input("Tamanho da lista: "))
print('\n')

#Chama a função do outro arquivo e cria a lista do tamanho solicitado.
novaLista = Lista(tamanho)
novaLista.Mostrar()
print('\n')

#Cria um loop para o usuario digitar os elementos e adiciona eles na lista.
for i in range(tamanho):
    produto = str(input(f"Produto {i}: "))
    posição = i
    novaLista.Inserir(produto, posição)
    posição = posição + 1
novaLista.Mostrar()
print('\n')

#Cria um loop para o usuario poder pesquisar dentro da sua lista e informa o elemento solictado.
#Caso o usuario não queira pesquisar nenhum elemento ele pode pular essa etapa.
for i in range(tamanho):
    buscar = 'Y'
    buscar = str(input("Você deseja buscar algum elemento da lista (Y/N): "))
    if (buscar == 'n' or buscar == 'N'):
        break
    else:
        pos = int(input(f'Digite a posição do que você deseja buscar, de 0 até {tamanho-1}: '))
        elemento = novaLista.Procurar(pos)
        print(f'O produto da posição {pos} é {elemento}.')
print('\n')

#Cria um loop para o usuario remover quantos elementos ele quiser e depois mostra a lista com as modificações.
#Caso o usuario não queira remover nenhum elemento ele pode pular essa etapa.
for i in range(tamanho):
    remover = 'Y'
    remover = str(input("Você deseja remover algum elemento da lista (Y/N): "))
    if (remover == 'n' or remover == 'N'):
        break
    else:
        pos = int(input(f'Digite a posição do elemento que você deseja remover, de 0 até {tamanho-1}: '))
        info = novaLista.Procurar(pos)
        elemento = novaLista.Remover(pos)
        print(f'O produto {info} da posição {pos} foi removido.')
        print('Nova lista:')
        novaLista.Mostrar()
print('\n')

#Pergunta ao usuario se ele deseja destruir a lista e depois encerra o programa.
limpar = "Y"
limpar = str(input('Você deseja limpar todos os elementos da lista (Y/N): '))
if (limpar == 'n' or limpar == 'N'):
    quit
else:
    novaLista.Limpar()
print('\n')
novaLista.Mostrar()
       