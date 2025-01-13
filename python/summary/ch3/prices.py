# 초단위 주식가격 배열이 주어졌을때,
# 각 가격의 떨어지지 않은 기간을 반환하는 함수 작성
# prices = [1, 2, 3, 2, 3]
# answer = [4, 3, 1, 1, 0]
from collections import deque

prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    queue = deque(prices)
    answer = []
    # queue 에 아무것도 남아있지 않을때까지
    while queue:
        current_target = queue.popleft()
        queue_to_compare = deque(queue)
        count = 0
        if len(queue) == 0:  # 마지막 요소인 경우
            answer.append(count)
            break
        else:
            # queue.append(current_target)  # 일단 현재 타겟 넣어두고
            while True:
                if len(queue_to_compare) == 0:
                    break
                compared_target = queue_to_compare.popleft()
                # print(f"queue_to_compare : {queue_to_compare}")
                if current_target > compared_target:  # 가격이 떨어진경우
                    count += 1
                    break
                else:
                    count += 1
            answer.append(count)
    return answer


def get_price_not_fall_periods_2(prices):
    queue = deque(prices)
    answer = []
    # queue 에 아무것도 남아있지 않을때까지
    while queue:
        current_target = queue.popleft()
        count = 0
        for next in queue:
            if current_target <= next:
                count += 1
            else:
                count += 1
                break
        answer.append(count)

    return answer


def get_price_not_fall_periods_3(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(0, n - 1):
        count = 0
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break

        answer[i] = count
    return answer


# sol 1,2,3 사이 시간복잡도 차이는 없다. 그냥 다르게 표현해본것
# 1. queue 두개
# 2. queue 하나
# 3. 이중 for

print(
    "정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods([1, 2, 3, 2, 3]),
)
print(
    "정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]),
)
print(
    "정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]),
)

print(
    "정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods_2([1, 2, 3, 2, 3]),
)
print(
    "정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods_2([3, 9, 9, 3, 5, 7, 2]),
)
print(
    "정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods_2([1, 5, 3, 6, 7, 6, 5]),
)

print(
    "정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods_3([1, 2, 3, 2, 3]),
)
print(
    "정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods_3([3, 9, 9, 3, 5, 7, 2]),
)
print(
    "정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ",
    get_price_not_fall_periods_3([1, 5, 3, 6, 7, 6, 5]),
)
