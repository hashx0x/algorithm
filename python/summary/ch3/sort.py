# sort
# 1. bubble sort
# 2. selection sort
# 3. insertion sort


def bubble_sort(array: list[int]):
    array_len = len(array)
    # 바로 옆의 값과만 비교하여 한 라운드에 최대 또는 최소값이 한쪽으로 몰리게됨
    # 위 과정을 반복
    # 총 라운드 i: array len - 1 첫라운드부터 하나씩 정렬
    # 내부 라운드 j: i 가 커짐에 따라 i 만큼 감소
    for i in range(array_len - 1):
        for j in range(array_len - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort_move_to_end(array: list[int]):
    # 한 라운드를 돌면서 최소 또는 최대값 기억해뒀다가 라운드 끝날때 위치 결정
    # 내부 라운드는 i 가 커짐에 따라 감소
    # 위 과정 반복
    # 0 1 2 3 4
    # 처음 :   4 6 2 9 1
    # i = 0 : 4 6 2 1 9  j = 0,1,2,3,4
    # i = 1 : 4 1 2 6 9  j = 0,1,2,3
    # i = 2 : 2 1 4 6 9
    # i = 3 : 1 2 4 6 9

    # 최대값 기준으로 끝자리와 계속 위치 swap
    # 첫번째 자리와 스왑도 가능
    array_len = len(array)
    for i in range(array_len - 1):
        max_index = 0
        for j in range(array_len - i):
            if array[j] > array[max_index]:
                max_index = j

        array[max_index], array[array_len - 1 - i] = (
            array[array_len - 1 - i],
            array[max_index],
        )

    return array


def selection_sort_move_to_first(array: list[int]):
    array_len = len(array)
    # 최소값을 i 로 가져온다.
    for i in range(array_len - 1):  # i : 총 4라운드 필요
        min_index = i
        for j in range(array_len - i):  # j : 0 ~ 4 - i
            if array[i + j] < array[min_index]:  # j는 항상 i 번째 index부터 시작
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def insertion_sort(array: list[int]):
    # 4 6 2 9 1 <-- 4는 정렬된걸로 본다.
    #   v
    # 4 6 2 9 1
    #     v
    # 4 6 2 9 1

    array_len = len(array)
    for i in range(array_len - 1):
        for j in range(i + 1, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break

    # 다른 형식의 Loop
    # for i in range(1, array_len):
    #     for j in range(i):  # 각 단계에서 i만큼의 비교, 스왑 연산을 해야함
    #         if array[i - j - 1] > array[i - j]:
    #             array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
    #         else:
    #             break

    return array


def insertion_sort_while(array: list[int]):
    array_len = len(array)

    for i in range(array_len - 1):
        current_target = array[i + 1]  # 현재 삽입 및 정렬할 요소
        j = i  # j를 하나씩 빼가면서 수행할 것
        while j >= 0 and array[j] > current_target:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_target

    return array


print(
    "bubble sort : 정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",
    bubble_sort([4, 6, 2, 9, 1]),
)
print(
    "bubble sort : 정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", bubble_sort([3, -1, 17, 9])
)
print(
    "bubble sort : 정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",
    bubble_sort([100, 56, -3, 32, 44]),
)

print(
    "selection_sort_move_to_end : 정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",
    selection_sort_move_to_end([4, 6, 2, 9, 1]),
)
print(
    "selection_sort_move_to_end : 정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",
    selection_sort_move_to_end([3, -1, 17, 9]),
)
print(
    "selection_sort_move_to_end : 정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",
    selection_sort_move_to_end([100, 56, -3, 32, 44]),
)


print(
    "selection_sort_move_to_first : 정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",
    selection_sort_move_to_first([4, 6, 2, 9, 1]),
)
print(
    "selection_sort_move_to_first : 정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",
    selection_sort_move_to_first([3, -1, 17, 9]),
)
print(
    "selection_sort_move_to_first : 정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",
    selection_sort_move_to_first([100, 56, -3, 32, 44]),
)

print(
    "insertion_sort : 정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",
    insertion_sort([4, 6, 2, 9, 1]),
)
print(
    "insertion_sort : 정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",
    insertion_sort([3, -1, 17, 9]),
)
print(
    "insertion_sort : 정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",
    insertion_sort([100, 56, -3, 32, 44]),
)

print(
    "insertion_sort_while : 정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",
    insertion_sort_while([4, 6, 2, 9, 1]),
)
print(
    "insertion_sort_while : 정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",
    insertion_sort_while([3, -1, 17, 9]),
)
print(
    "insertion_sort_while : 정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",
    insertion_sort_while([100, 56, -3, 32, 44]),
)
