# 부모의 값이 항상 자식보다 크거나 낮은상황
# 정렬되어있는 상황


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        last_idx = len(self.items) - 1

        while last_idx > 1 and self.items[last_idx] > self.items[last_idx // 2]:
            self.items[last_idx], self.items[last_idx // 2] = (
                self.items[last_idx // 2],
                self.items[last_idx],
            )

            last_idx //= 2

    def delete(self):
        # 루트노드와 마지막 요소 교환
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # pop
        root_node = self.items.pop()

        length = len(self.items)
        cur_idx = 1
        # 교환된 마지막요소 자리 찾아주기
        while cur_idx < length - 1:
            # 자식값들과 크기 비교해가면서 교환
            left_child_idx = cur_idx * 2
            right_child_idx = cur_idx * 2 + 1
            # 최대 값의 idx 를 일단 현재 idx 로 설정
            max_idx = cur_idx

            # 자식노드 값들과 크기 비교 후 max_idx 업데이트
            if (
                left_child_idx <= length - 1
                and self.items[max_idx] < self.items[left_child_idx]
            ):
                max_idx = left_child_idx
            if (
                right_child_idx <= length - 1
                and self.items[max_idx] < self.items[right_child_idx]
            ):
                max_idx = right_child_idx

            # max idx 가 cur_idx 와 같은경우 -> 교환이 일어나지 않아도 되므로 현재 자리가 맞다. -> break
            if max_idx == cur_idx:
                break

            # 자리 교환
            self.items[cur_idx], self.items[max_idx] = (
                self.items[max_idx],
                self.items[cur_idx],
            )

            # 다음 루프 위해 cur_idx 업데이트
            cur_idx = max_idx

        return root_node


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

max_heap.delete()
print(max_heap.items)

# max_heap = MaxHeap()
# max_heap.insert(3)
# max_heap.insert(5)
# max_heap.insert(4)
# # max_heap.insert(9)
# print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
