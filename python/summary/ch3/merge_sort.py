def merge(array1: list[int], array2: list[int]):

    array1_idx = 0
    array2_idx = 0

    result: list[int] = []

    # 두 배열 비교하면서 result 에 append
    while array1_idx < len(array1) and array2_idx < len(array2):
        if array1[array1_idx] <= array2[array2_idx]:
            result.append(array1[array1_idx])
            array1_idx += 1
        else:
            result.append(array2[array2_idx])
            array2_idx += 1

    # 두 배열 중 남은 요소가 있는 배열 처리
    if array2_idx == len(array2):
        while array1_idx < len(array1):
            result.append(array1[array1_idx])
            array1_idx += 1
    if array1_idx == len(array1):
        while array2_idx < len(array2):
            result.append(array2[array2_idx])
            array2_idx += 1

    return result


# 시간복잡도 N*logN
def merge_sort(array: list[int]):
    if len(array) == 1:
        return array

    mid_idx = len(array) // 2

    # 재귀동작
    array1 = merge_sort(array[:mid_idx])
    array2 = merge_sort(array[mid_idx:])

    # 현 스택에서 재귀 끝나면 머지처리
    return merge(array1, array2)


print(
    "정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ",
    merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]),
)
print(
    "정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ",
    merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]),
)
print(
    "정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ",
    merge_sort([-1, -1, 0, 1, 6, 9, 10]),
)
