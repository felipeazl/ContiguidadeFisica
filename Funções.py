#Arquivo com as funções usadas para a manipulação da lista.

class Lista:
    
    #Função para criar a lista, o tamanho dela é dado pelo usuario no arquivo 'Lista.py'.
    def __init__(self, tamanho):
        self.elemento = [None] * tamanho
        self.inicio = 0
        self.fim = -1
        self.tamanho = tamanho
    
    #Função para exibir todos os elementos da lista. 
    def Mostrar(self):
        auxLista = self.inicio
        if (auxLista == -1):
            print("A lista está vazia.")
        else:
            print(self.elemento)
    
    #Função que busca o elemento da lista, na posição indicada pelo usuario, e retorna ele.
    def Procurar(self, posição):
        if ((posição > self.fim - self.inicio) or (posição < 0)):
            return False
        else:
            return self.elemento[self.inicio + posição]
    
    #Função que coloca os elementos digitados pelo usuario na lista. Pegando como parametro o nome do elemento e a sua posição. 
    def Inserir(self, valor, posição):
        if ((posição > self.tamanho - 1) or ((posição < self.inicio) and (posição > self.fim - 1))):
            print("ERRO: posição invalida.")
        else:
            if self.inicio == -1:
                self.fim = 0
                for i in range(self.inicio, self.inicio + posição):
                    self.elemento[i - 1] = self.elemento[i]
                    self.inicio = self.inicio - 1
            self.elemento[self.inicio + posição] = valor
    
    #Função que remove um elemento da lista de acordo com a posição digitada pelo usuario.
    #Essa função mantem o espaço do elemento removido e o substitui por "None".    
    def Remover(self, posição):
        if((posição > self.fim - self.inicio) or (posição < 0)):
            print("ERRO: posição invalida.")
        else:
            self.elemento[self.inicio + posição] = None
    
    #Função que destroi a lista. 
    def Limpar(self):
        self.elemento = None
        self.inicio = 0
        self.fim = -1
        self.tamanho = 0