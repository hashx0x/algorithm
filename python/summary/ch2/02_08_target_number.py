from collections import defaultdict

# target number
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# e.g.
# numbers = [2,1,3]
# +2 +1 +3  6
#       -3  0
#    -1 +3  4
#       -3  -2
# -2 +1 +3  2
#       -3  -4
#    -1 +3  0
#       -3  -6


# 점화식관계 풀이 방법
# dfs, bfs, dp
def dfs(
    array,
    target,
    current_idx,
    cur_sum,
):
    if current_idx == len(array):
        return 1 if target == cur_sum else 0

    plus_case = dfs(
        array,
        target,
        current_idx=current_idx + 1,
        cur_sum=cur_sum + array[current_idx],
    )
    minus_case = dfs(
        array,
        target,
        current_idx=current_idx + 1,
        cur_sum=cur_sum - array[current_idx],
    )
    return plus_case + minus_case


def target_number_dfs(array, target):

    return dfs(array, target, 0, 0)


# n-1 번째 합 -> n번째 원소를 더하거나 빼거나
def target_number_dp(array, target):
    # dp[합] = 이 합을 만드는 경우의 수
    dp = defaultdict(int)
    dp[0] = 1  # 아무 숫자도 사용하지 않았을 때 합=0을 만드는 경우 1개
    print(f"dp init : {dp}")
    for num in array:
        new_dp = defaultdict(int)
        for current_sum, count in dp.items():
            # +num을 더한 합
            new_dp[current_sum + num] += count
            # -num을 뺀 합
            new_dp[current_sum - num] += count
        print(f"current num : {num}, dp: {new_dp} ")
        dp = new_dp  # 갱신
    print(f"dp: {dp}")
    return dp[target]


# print(target_number_dfs([1, 1, 1, 1, 1], 3))
# print(target_number_dfs([4, 1, 2, 1], 4))
# print(target_number_dfs([1, 1, 2, 5], 3))


# print(target_number_dp([1, 1, 1, 1, 1], 3))
# print(target_number_dp([4, 1, 2, 1], 4))
print(target_number_dp([1, 1, 2, 5], 3))
