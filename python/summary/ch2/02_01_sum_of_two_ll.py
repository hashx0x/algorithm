# sum of two linked list
from ...tip.linked_list import Node, LinkedList

# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)


def get_all_nodes_value(linked_list: LinkedList):
    linked_list_cur_node = linked_list.get_node(0)
    value = 0

    while linked_list_cur_node is not None:  # None 으로 노드존재여부확인
        value = (10 * value) + linked_list_cur_node.data
        linked_list_cur_node = linked_list_cur_node.next

    return value


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = get_all_nodes_value(linked_list_1)
    sum_2 = get_all_nodes_value(linked_list_2)

    return sum_1 + sum_2


print(get_linked_list_sum(linked_list_1, linked_list_2))
