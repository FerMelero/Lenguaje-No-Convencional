class Stack:
    def __init__(self, max_size):
        self.__stackList = [None] * max_size
        self.__top = -1

    # Inserta un elemento en la pila
    def push(self, item):
        if self.isFull():
            raise IndexError("Stack is full")
        self.__top += 1
        self.__stackList[self.__top] = item

    # Elimina y devuelve el elemento superior
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        top = self.__stackList[self.__top]
        self.__stackList[self.__top] = None
        self.__top -= 1
        return top

    # Devuelve True si la pila está vacía
    def isEmpty(self):
        return self.__top < 0

    # Devuelve True si la pila está llena
    def isFull(self):
        return self.__top >= len(self.__stackList) - 1

    # Devuelve el elemento en la cima sin eliminarlo
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.__stackList[self.__top]

    # Devuelve el número de elementos
    def __len__(self):
        return self.__top + 1

    # Representación en cadena de la pila
    def __str__(self):
        elementos = [str(self.__stackList[i]) for i in range(self.__top + 1)]
        return "[" + ", ".join(elementos) + "]"
