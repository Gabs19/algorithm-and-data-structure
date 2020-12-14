from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self,e):
        if self.head:
            #inserção quando já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(e)
        else:
            #primeira inserção na lista
            self.head = Node(e)
        self._size = self._size + 1

    #usar a função nativa da linguagem
    def __len__(self):
        #retorna o tamanho da lista
        return self._size
    
    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        return pointer
     
     #sobrecarga de operador
     #funções especiais do python, podendo usar as anotações de colchetes
    def __getitem__(self, index):
        pointer  = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError('list index out of range')
    
    def __setitem__(self, index, e):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = e
        else:
            raise IndexError('list index out of range')

    def index(self, e):
        #retorna o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == e:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError(f'{e} is not in list')
    
    def insert(self, index, e):
        if index == 0:
            node = Node(e)
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index - 1)
            node.next = pointer.next #antes de ligar com antecessor, ligamos aos que vem após
            pointer.next = node
        self._size = self._size + 1                 

    def remove(self, e):
        if self.head == None:
            raise ValueError(f'{e} is not in list')
        elif self.head.data == e:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == e:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
                self._size = self._size - 1
            return True
        raise ValueError(f'{e} is not in list')
    
    def __repr__(self):
        r = ''
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + ' '
            pointer = pointer.next
        listaPrint = f'[{r}]'
        return listaPrint

    def __str__(self):
        return self.__repr__()
