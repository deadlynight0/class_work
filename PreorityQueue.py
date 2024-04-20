class AvengersPriorityQueue:
    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None

    class Node:
        def __init__(self,data,prev):
            self.data = data
            self.prev = prev

class AvengersMission:
    def __init__(self, description, preority = 3):
        self.__description = description
        self.__preority = preority


