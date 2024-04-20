class AvengersPriorityQueue:
    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None

    class Node:
        def __init__(self,data,prev):
            self.data = data
            self.prev = prev

    def enqueue(self,mission):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def get_count(self):
        return self.__count

    class AvengersMission:
        def __init__(self, description, preority = 3):
            self.__description = description
            self.__preority = preority


