from node import Node

class Stack:
    
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, e):
        #insere um elemento na pilha
        #complexidade O[1]
        node = Node(e)
        node.next = self.top
        self.top = node 
        self._size = self._size + 1

    def pop(self):
        #remove o elemento do topo da pilha
        #complexidade O[1]
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        else:
            raise IndexError('The stack is empty')

    def peek(self):
        #retorna do topo da pilha sem remover
        #complexidade O[1]
        if self._size > 0:
            return  self.top.data
        else:
            raise IndexError('The stack is empty')

    #usar a função nativa da linguagem
    def __len__(self):
        #retorna o tamanho da lista
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()