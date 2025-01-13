top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    stack = heights
    answer = [0] * len(heights)
    cur_start_idx = len(heights) - 1  # 4

    while stack:
        cur = stack.pop()  # len 감소
        n = len(stack)
        if n == 0:
            answer[0] = 0
            break
        if cur >= stack[n - 1]:  # 작거나 같으면 넘긴다. #3
            continue
        else:  # 크면
            for i in range(cur_start_idx, n - 1, -1):
                answer[i] = n
            cur_start_idx = n - 1
    # print(answer)
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4]

print(
    "정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders([6, 9, 5, 7, 4])
)
print(
    "정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",
    get_receiver_top_orders([3, 9, 9, 3, 5, 7, 2]),
)
print(
    "정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",
    get_receiver_top_orders([1, 5, 3, 6, 7, 6, 5]),
)
