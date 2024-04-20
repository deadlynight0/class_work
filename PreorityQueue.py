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

        if self.__count == 0:
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node
        self.__count += 1


    def __bubble_sort(self):
        if self.__head is None:return

        for i in range(self.__count):
            pass






    def dequeue(self):
        if self.__count == 0:
            raise Exception("Exception type: queue is empty")

        data = self.__head.data
        self.__head = self.__head.prev

        self.__count -= 1

        if self.__count == 0:
            self.__tail = None

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


    def __str__(self):
        return f"Description: {self._description}, ID: {self._priority}"


c1 = AvengersPriorityQueue()
mission1 = AvengersMission('A',2)
mission2 = AvengersMission('B',1)
mission3 = AvengersMission('C',3)

c1.enqueue(mission1)
print('Enqueue: ', mission1)

c1.enqueue(mission2)
print('Enqueue: ', mission2)

c1.enqueue(mission3)
print('Enqueue: ', mission3)


print(c1.dequeue())
print(c1.dequeue())
print(c1.dequeue())


