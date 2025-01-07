class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # sol 1 : 끝까지 탐색해서 길이 확정 후 다시 검색
    def get_kth_node_from_the_end(self, k):
        # 끝까지 탐색하면서 길이 수집
        cur_node = self.head
        idx = 0  # idx = length - 1

        while cur_node.next:
            cur_node = cur_node.next
            idx += 1

        # 처음부터 idx - (k -1) 번 인덱스의 노드 찾아서 반환
        target_node = self.head
        cur_idx = 0
        while cur_idx != (idx - (k - 1)):
            target_node = target_node.next
            cur_idx += 1

        return target_node

    # sol 2 : two pointer
    def get_kth_node_from_the_end_two_pointer(self, k):
        # two pointer setting
        cur_node = self.head
        fast_node = self.head
        for i in range(k - 1):
            fast_node = fast_node.next

        while fast_node.next is not None:
            cur_node = cur_node.next
            fast_node = fast_node.next

        return cur_node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

print(linked_list.get_kth_node_from_last(2).data)
print(linked_list.get_kth_node_from_last_two_pointer(3).data)
