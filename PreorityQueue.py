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
        node = AvengersPriorityQueue.Node(mission,None)

        if mission._priority == 1:
            self.__head = node
            self.__tail = node
            self.__count += 1

        if mission._priority == 2 and self.__tail == None:
            self.__tail.data = node
            self.__count += 1

        if mission._priority == 2 and self.__tail != None:
            self.__head.data = node
            self.__head.prev = node
            self.__count += 1

        if mission._priority == 3:
            self.__tail.data = node
            self.__head.prev = node
            self.__count += 1


    def dequeue(self):
        if self.__count == 0: return "Элементов нет"
        data = self.__head.data
        self.__head = self.__head.prev
        self.__count -= 1
        if self.__count == 0: self.__tail = None
        return data

    def peek(self):
        return self.__head.data if self.__head != None else None

    def is_empty(self):
        return self.__count == 0

    def get_count(self):
        return self.__count

    class AvengersMission:
        def __init__(self, description,priority = 3):
            self._description = description
            self._priority = priority


c1 = AvengersPriorityQueue()
mission = AvengersPriorityQueue.AvengersMission('1213214',1)
c1.enqueue(mission)
mission = AvengersPriorityQueue.AvengersMission('1213214',3)
c1.enqueue(mission)
print(c1.peek())
print(c1.dequeue())
print(c1.peek)
print(c1.dequeue())
print(c1.peek())
print(c1.dequeue())


