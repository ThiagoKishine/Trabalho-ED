'Nome: Thiago Matheus Kiyoshi Kishine'
'RA: G267HF4'
'Turma: CC4P12'

# Criando uma classe Nodo
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None
        
    def get_data(self):
        return self.dado

    def get_next(self):
        return self.proximo

    def set_data(self, novodado):
        self.dado = novodado

    def set_next(self, novoproximo):
        self.proximo = novoproximo
        
# Criando uma classe Lista duplamente encadeada:
class lista_duplamente:
    def __init__(self):
        self.cabeca = None
        self.rabo = None
        
# Número de elementos da lista
    def getCount(self):
        Nodo = self.cabeca  
        count = 0  
 
        # Loop quando o fim da lista não é alcançado
        while (Nodo):
            count += 1
            Nodo = Nodo.proximo
        return count
        
# Definindo o metodo push para adicionar elementos no começo
    def push(self, valor):
        NovoNodo = Nodo(valor)
        NovoNodo.set_next = self.cabeca
        if self.cabeca is not None:
            self.cabeca.anterior = NovoNodo
        self.cabeca = NovoNodo
    
# Modo de busca
    def search(self, ldlista, key):
 
        # Cso básico
        if(not ldlista):
            return False
 
        # Se key é presente, retorna True
        if(ldlista.dado == key):
            return True
 
        # Recorre para o restante da lista
        return self.search(ldlista.proximo, key)
        
# Definir o append para adicionar elementos no final
    def append(self, valor):
        NovoNodo = Nodo(valor)
        NovoNodo.proximo = None
        if self.cabeca is None:
            NovoNodo.anterior = None
            self.cabeca = NovoNodo
            return
        final = self.cabeca
        while (final.proximo is not None):
            final = final.proximo
        final.proximo = NovoNodo
        NovoNodo.anterior = final
        return
         
# Definindo função delete de Nodos   
    def deleteNodo(self, delet):
         
        # Caso básico
        if self.cabeca is None or delet is None:
            return
         
        # Se o nodo escolhido for a "cabeça"
        if self.cabeca == delet:
            self.cabeca = delet.proximo
 
        # Altera o próximo apenas se o nodo a ser excluído NÃO for o ultimo nodo
        if delet.proximo is not None:
            delet.proximo.anterior = delet.anterior
     
        # Altera o anterior apenas se o nodo a ser excluído NÃO for o primeiro nodo
        if delet.anterior is not None:
            delet.anterior.proximo = delet.proximo
 
    # Dando referência ao cabeçalho de uma lista
    def push(self, NovoNodo):
  
        # 1. Aloca os nodos
        # 2. Coloca os dados nele
        NovoNodo = Nodo(NovoNodo)
  
        # 3. Faz o próximo do novo nodo como "cabeça" e o anterior como None
        NovoNodo.proximo = self.cabeca
  
        # 4. Altera o anterior do nodo principal para NovoNodo
        if self.cabeca is not None:
            self.cabeca.anterior = NovoNodo
  
        # 5. Faz a "cabeça" apontar para o novo nodo
        self.cabeca = NovoNodo
        
# Metodo de busca pelo valor de sua posição
    def getNth(self, index):
        atual = self.cabeca 
        # Index do nodo atual
        count = 0  
 
        # Loop quando o fim da lista não é alcançado
        while (atual):
            if (count == index):
                return atual.dado
            count += 1
            atual = atual.proximo
 
        # Caso o usuario coloque um valor inexistente
        assert(false)
        return 0
        
# Deletando o ultimo valor da lista
    def _pop_(self):
        if(self.cabeca != None):
            if(self.cabeca.proximo == None):
                self.cabeca = None
            else:
                Nodo = self.cabeca
                while(Nodo.proximo.proximo != None):
                    Nodo = Nodo.proximo
                final = Nodo.proximo
                Nodo.proximo = None
                final = None
    
# Deletando um valor especificado            
    def deleteNodo(self, key):
 
        Nodo = self.cabeca
 
        # Se a "cabeça" tiver o valor excluído
        if (Nodo is not None):
            if (Nodo.dado == key):
                self.cabeca = Nodo.proximo
                Nodo = None
                return
 
        # Procura o valor a ser excluido, acompanhando o anterior para que possa ser alterado
        while(Nodo is not None):
            if Nodo.dado == key:
                break
            anterior = Nodo
            Nodo = Nodo.proximo
 
        # Se o valor não estiver presente na lista
        if(Nodo == None):
            return
 
        # Desvincula da lista
        anterior.proximo = Nodo.proximo
 
        Dado = None
        
# Removendo um valor pela sua posição
    def deleteNodeAtGivenPosition(self, position):
        if self.cabeca is None:
            return
        index = 0
        atual = self.cabeca
        while atual.proximo and index < position:
            anterior = atual
            atual = atual.proximo
            index += 1
        if index < position:
            print("\nIndex está fora do alcance.")
        elif index == 0:
            self.cabeca = self.cabeca.proximo
        else:
            anterior.proximo = atual.proximo
            
#Definindo os dados dos nodos em um indice especifico
    def set(self, index, novodado):
        atual = self.cabeca
        anterior = None
        for i in range(index):
            anterior = atual
            atual = atual.get_next()
        if atual != None:
            NovoNodo = Nodo(novodado)
            NovoNodo.set_next(atual)
            if anterior is None:
                self.cabeca = NovoNodo
            else:
                anterior.set_next(NovoNodo)
        else:
            raise("fora do alcance")

#Metodo de printar a lista   
    def listaprint(self):
        result = "["
        Nodo = self.cabeca
        if Nodo != None:
            result += str(Nodo.dado)
            Nodo = Nodo.proximo
            while Nodo:
                result += ", " + str(Nodo.dado)
                Nodo = Nodo.proximo
        result += "]"
        return print(result)
        

ldlista = lista_duplamente()
ldlista.push(12)
ldlista.append(9)
ldlista.push(8)
ldlista.push(62)
ldlista.append(45)
ldlista.set(2, 13)


print('Nome: Thiago Matheus Kiyoshi Kishine')
print('RA: G267HF4')
print('Turma: CC4P12')
print('')
print('--------------------- MENU ---------------------')
print('1) Inserir item na primeira posição') 
print('2) Inserir item na última posição')
print('3) Inserir item em determinada posição')
print('4) Buscar item de determinada posição')
print('5) Buscar item por elemento')
print('6) Remover item da primeira posição')
print('7) Remover item da última posição')
print('8) Remover item de determinada posição')
print('9) Remover determinado elemento')
print('10) Exibir a quantidade de elementos na lista')
print('11) Exibir os elementos da lista')
print('0) Sair do Menu')
print('--------------------- MENU ---------------------')
print('')
selec = int(input('Digite a opção desejada: '))

if (selec > 11) or (selec < 0):
    print('Opção inválida')
else:
    if selec==1:
        print('Exercício 1')
        print('')
        add = int(input('Insira um número para ficar na primeira posição da lista: '))
        print('')
        ldlista.push(add)
        print('')
        print(ldlista.listaprint())
        
    if selec==2:
        print('Exercício 2')
        print('')
        add = int(input('Insira um número para ficar na última posição da lista: '))
        ldlista.append(add)
        print('')
        print(ldlista.listaprint())
        
    if selec==3:
        print('Exercício 3')
        print('')
        add = int(input('Insira a posição desejada: '))
        add2 = int(input('Insira um número para ser inserido: '))
        ldlista.set(add, add2)
        print(ldlista.listaprint())
        
    if selec==4:
        print('Exercício 4')
        print('')
        n = int(input('Insira uma posição para saber seu valor: '))
        print("O elemento dessa posição é:", ldlista.getNth(n))
        
        
    if selec==5:
        print('Exercício 5')
        print('')
        key = int(input('Insira o valor que deseja buscar: '))
        if ldlista.search(ldlista.cabeca, key):
            print("Esse elemento está na lista")
        else:
            print("Esse elemento não está na lista")
        
    if selec==6:
        print('Exercício 6')
        print('')
        ldlista.deleteNodo(ldlista.cabeca)
        print('Sua lista ficou assim: ')
        print(ldlista.listaprint())
        
    if selec==7:
        print('Exercício 7')
        print('')
        ldlista._pop_()
        print('Sua lista ficou assim: ')
        print(ldlista.listaprint())
        
    if selec==8:
        print('Exercício 8')
        print('')
        ldlista.listaprint()
        print("Lista atual: ")
        add = int(input('Insira a posição para remover seu valor: '))
        ldlista.deleteNodeAtGivenPosition(add)
        print("\nSua lista ficou assim: ")
        ldlista.listaprint()
        
    if selec==9:
        print('Exercício 9')
        print('')
        ldlista.listaprint()
        add = int(input("Qual valor deseja remover? "))
        ldlista.deleteNodo(add)
        print("\nLista depois da remoção: ")
        ldlista.listaprint()   
        
    if selec==10:
        print('Exercício 10')
        print('')
        print("Quantidade de valores é:", ldlista.getCount())
        
    if selec==11:
        print('Exercício 11')
        print('')
        print('Os elementos da lista são: ')
        print(ldlista.listaprint())
        
    if selec==0:
        exit()