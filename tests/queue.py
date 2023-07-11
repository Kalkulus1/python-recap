# from collections import deque

# my_queue = deque()

# my_queue.append(1)
# my_queue.append(5)
# my_queue.append(3)
# print(my_queue)
# print(my_queue.popleft())
# print(list(my_queue))


class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue):
            return self.queue.pop(0)
        return None
    
    def get_size(self):
        return len(self.queue)
    
    def __str__(self) -> str:
        return str(self.queue)
    
my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(3)
my_queue.enqueue(8)
print(my_queue)
print(my_queue.get_size())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.get_size())
print(my_queue.dequeue())
print(my_queue.dequeue())
