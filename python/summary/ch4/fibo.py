def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1

    n_minus_1 = fibo_recursion(n - 1)
    n_minus_2 = fibo_recursion(n - 2)

    return n_minus_1 + n_minus_2


# print(fibo_recursion(20))  # 6765


# 같은 연산을 반복한다. -> dp

memo = {1: 1, 2: 1}


def fibo_dp(n):
    # 메모값에 있다면 메모값 반환
    if n in memo:
        return memo[n]

    # 없으면 재귀호출로 구한다.
    nth = fibo_dp(n - 1) + fibo_dp(n - 2)
    # 값을 구하면 적어둔다.
    memo[n] = nth

    return nth


print(fibo_dp(100))
