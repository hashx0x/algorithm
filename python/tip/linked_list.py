# linked list
# 중간에 연결, 삭제 용이.
# 탐색 시간 소요

## node 내 정보 
# 1. data
# 2. pointer

# linked list 내 한 칸
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        
        
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    def append(self, value):
        current_node = self.head
        while current_node.next: # current_node 의 next 가 있다면
            current_node = current_node.next
        
        current_node.next = Node(value)
    
    def print_all(self):
        current_node = self.head
        
        while current_node: # current_node 가 있다면
            print(current_node.data)
            current_node = current_node.next
        
        
linked_list = LinkedList(5)
print(linked_list)

linked_list.append(12)
linked_list.append(8)

print("!!!!")
linked_list.print_all()