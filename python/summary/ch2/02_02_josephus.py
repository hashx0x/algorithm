# sum of two linked list
from ...tip.linked_list import Node, LinkedList
from collections import deque

# BOJ 1158

# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# # 마지막 node의 next는 head 다
# last_node = linked_list.get_node(n - 1)
# last_node.next = linked_list.head

# 0 1 2 3 4 5 6  -- index = value - 1
# *1 2 3 4 5 6 7    3
# 1 2 *4 5 6 7      6
# 1 2 4 5 *7        2
# 1 *4 5 7          7
# *1 4 5


def josephus_problem_sol_1(n, k):
    # linked list setting
    linked_list = LinkedList(1)
    for i in range(2, n + 1):
        linked_list.append(i)

    # 변수 세팅
    cur_length = n
    cur_index = 0
    answer = []

    while cur_length > 0:

        # 현재 K번재 인덱스 추적
        cur_index = (cur_index + (k - 1)) % cur_length

        # node get
        node = linked_list.get_node(cur_index)

        # node data answer 추가
        answer.append(node.data)

        # 해당노드 삭제
        linked_list.delete_node(cur_index)

        # 노드 길이 감소
        cur_length -= 1

    print(f"sol1 answer : {answer}")


def josephus_problem_sol_2(n, k):
    # queue 이용
    queue = deque([i for i in range(1, n + 1)])

    answer = []

    while len(queue):
        for i in range(k - 1):
            first = queue.popleft()
            queue.append(first)

        target = queue.popleft()
        answer.append(target)

    print(f"sol2 answer : {answer}")


# n, k = map(int, input().split())
# josephus_problem(n, k)
josephus_problem_sol_1(7, 3)
josephus_problem_sol_2(7, 3)
