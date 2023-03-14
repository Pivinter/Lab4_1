class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            
    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            print(current.data)
            while current.next != self.head:
                current = current.next
                print(current.data)
    
    def sum_positive(self):
        if self.head is None:
            return 0
        else:
            current = self.head
            sum = 0
            if current.data > 0:
                sum += current.data
            while current.next != self.head:
                current = current.next
                if current.data > 0:
                    sum += current.data
            return sum
        
circular_list = CircularLinkedList() #1
circular_list.append(5) #2
circular_list.append(-3) #3
circular_list.append(10) #4
circular_list.append(-7) #5
circular_list.print_list()
print("Sum:")
print(circular_list.sum_positive())
