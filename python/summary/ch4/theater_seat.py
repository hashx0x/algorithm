# 문제링크 : https://www.acmicpc.net/problem/2302

# 어떤 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다.
# 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다.
# 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
# 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고, 6번 좌석이나 8번 좌석에도 앉을 수 있다.
# 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.

# 그런데 이 극장에는 “VIP 회원”들이 있다. 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.

# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# VIP 회원들의 좌석 번호들이 주어졌을 때, 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 구하는 프로그램을 작성하시오.

# 예를 들어서, 그림과 같이 좌석이 9개이고,
# 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다. 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.


# reminder
# vip 기준에 따라 => 구간이 나뉘어진다 => 구간별로 나누어 경우의 수를 전부 곱하면 정답
# 구간별 경우의 수는 길이에 따라 경우의 수가 달라진다고 파악
# *** 낯선 수열에 대해 조사할때 ***
# 1. 일단 간단한 케이스들을 직접 해본다.
# 2. 숫자를 나열해가면서 규칙성 파악
# 3. 파악이 어려우면 점화관계 여부를 파악해본다.
# 길이에 따라 어떻게 달라질까 생각해보다 점화관계(앞선 결과가 뒤의 결과에 영향을 미치는 관계) 의심
# 피보나치 수열 발견 =>
# 길이 n일 경우에 대해 생각해보면
# 1. n-1 의 경우에서 n좌석에 n번 입장권을 가진 사람이 앉을 경우 => f(n-1) 의 경우의 수
# 2. n번 입장권 소유자와 n-1번 입장권 사람이 바꿔 앉을 경우 => f(n-2) 의 경우의 수
# 두가지로 케이스로 분류가 가능하다.
# 따라서 f(n) = f(n-1) + f(n-2)


def get_all_ways_of_theater_seat(total_count: int, fixed_seat_array: list[int]):
    memo = {1: 1, 2: 2}

    # fibo 함수 세팅
    def fibo(n: int):
        if n in memo:
            return memo[n]

        answer = fibo(n - 1) + fibo(n - 2)
        memo[n] = answer
        return answer

    # vip 기준으로 배열 쪼개기
    # [2,4,7]
    fixed_seat_array.append(total_count + 1)
    #  0 1 2  3
    # [2,4,7,10]
    # print(f"fixed_seat_array: {fixed_seat_array}")

    length_list: list[int] = []

    len_fixed_seat_array = len(fixed_seat_array)  # 4
    # [1,1,2,2]
    for i in range(0, len_fixed_seat_array):
        if i == 0:
            length_list.append(fixed_seat_array[i] - 0 - 1)
        if i == len_fixed_seat_array - 1:  # i 가 마지막 원소일때
            break
        length_list.append(fixed_seat_array[i + 1] - fixed_seat_array[i] - 1)

    # print(f"lenth_list : {length_list}")
    answer = 0
    for length in length_list:
        if answer == 0:
            answer += fibo(length)
        else:
            answer *= fibo(length)

    return answer


#   v   v     v
# 1 2 3 4 5 6 7 8 9
# (2 - 0 - 1), (4 - 2 - 1), (7 - 4 - 1), (n+1 - 7 - 1)
print("정답 = 12 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [4, 7]))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
# print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
# print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))
