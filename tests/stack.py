class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        return None
    
    def peek(self):
        if len(self.stack):
            return self.stack[len(self.stack)-1]
        return None
    
    def __str__(self) -> str:
        return str(self.stack)


my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.peek())