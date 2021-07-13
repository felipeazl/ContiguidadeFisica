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
    
    #Função que coloca os elementos digitados pelo usuario na lista. Os elementos sempre sao adicionados de forma sucessiva, ou seja, o primeiro
    #elemento digitado vai ser o primeiro da lista, o segundo digitado sera o segundo da lista e continua ate preencher todos os espaçoes da lista   
    def Inserir(self, valor, posição):
        if (((self.inicio == 0) and (self.fim == self.tamanho - 1)) or (posição < 0) or (((self.inicio == -1) and (posição != 0)))):
            print("ERRO: posiçao invalida.")
        else:
            if (self.inicio == -1):
                self.inicio = 0
                self.fim = 0
            else:
                if(self.fim != self.tamanho - 1):
                    for i in range (self.fim, self.inicio + posição - 1, - 1):
                        self.elemento[i+1] = self.elemento[i]
                    self.fim = self.fim + 1
                else:
                    for i in range(self.inicio, self.inicio + posição):
                        self.element[i-1] = self.elemento[1]
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