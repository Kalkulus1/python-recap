class Node:
    """
    Node Class
    """
    def __init__(self, d, n=None, p=None) -> None:
        self.data = d
        self.next_node = n
        self.prev_node = p
    
    def __str__(self) -> str:
        return f"({self.data})"


class LinkedList:
    def __init__(self, r=None) -> None:
        self.root = None
        self.size = 0
    
    def add(self, d):
        new_node = Node(d=d, n=self.root)
        self.root =  new_node
        self.size += 1
    
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    
    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next_node
        print("None")
                
    
my_list = LinkedList()
my_list.add(2)
my_list.add(8)
my_list.add(12)
my_list.print_list()

print(my_list.size)
my_list.remove(8)
print(my_list.size)
my_list.print_list()
print(my_list.find(2))
print(my_list.root)
