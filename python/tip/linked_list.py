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
    
    # 맨 끝에 요소추가 
    def append(self, value):
        current_node = self.head
        while current_node.next: # current_node 의 next 가 있다면
            current_node = current_node.next
        
        current_node.next = Node(value)
    
    # 링크드리스트 data 모두 출력
    def print_all(self):
        current_node = self.head
        
        while current_node: # current_node 가 있다면
            print(current_node.data)
            current_node = current_node.next
    
    # n번째 요소반환
    def get_node(self, index) -> Node:
        cur = self.head
        cur_idx = 0
        
        while cur_idx is not index:
            cur = cur.next
            cur_idx += 1
        
        return cur
    
    # n번째 인덱스에 요소추가
    def add_node(self, index, value):
        if index == 0:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            
        else:
            cur = self.head
            cur_idx = 0
            
            while cur_idx is not index - 1:
                cur = cur.next
                cur_idx += 1
            
            temp_node = cur.next
            cur.next = Node(value)
            cur.next.next = temp_node
    
    def add_node2(self, index, value):
        # index = 0 인 경우
        if index == 0:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        else:
            new_node = Node(value)
            # index - 1 의 노드가 필요하다.
            prev_node = self.get_node(index-1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node
    
    def delete_node(self, index):
        # [5] -> [6] -> [12] -> [8] 에서 요소를 삭제한다면
        index_node = self.get_node(index)
        if index == 0:
            self.head = self.get_node(1)
        else:
            # 삭제하려는 노드가 맨 끝 노드여도 prev_node.next 는 None으로 세팅된다.
            prev_node = self.get_node(index-1) 
            prev_node.next = index_node.next 
            # 다른 방법
            # next_node = self.get_node(index+1)
            # prev_node.next = next_node
        
        
        
linked_list = LinkedList(5)
print(linked_list)

linked_list.append(12)
linked_list.append(8)

print("!!!!")
linked_list.print_all()

linked_list.add_node2(1, 6)
print("here")
linked_list.print_all()