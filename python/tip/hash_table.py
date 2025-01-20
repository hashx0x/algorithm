class Dict:
    def __init__(self) -> None:
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = index = hash(key) % len(self.items)
        return self.items[index]


# collision 발생(index 중복) 시 해결
# 1. chaining : items 한 요소를 linked list 로 구현
# 2. 개방주소법 : 있으면 그 다음칸, 다음칸 이동하며 빈자리에 매핑


class LinkedTuple:
    def __init__(self) -> None:
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v


class ChainingDict:
    def __init__(self) -> None:
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        linked_tuple = self.items[index]
        linked_tuple.add(key, value)

    def get(self, key):
        index = index = hash(key) % len(self.items)
        linked_tuple = self.items[index]
        return linked_tuple.get(key)
