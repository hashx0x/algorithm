# 문제링크 : https://www.acmicpc.net/problem/14503

# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

# 로봇 청소기가 있는 방은
# N * M  크기의 직사각형으로 나타낼 수 있으며,
# 1 * 1 크기의 정사각형 칸으로 나누어져 있다.
# 각각의 칸은 벽 또는 빈 칸이다.
# 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표
# (r, c)로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가
# (0, 0), 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 (N-1, M-1)이다. 즉, 좌표
# (r, c)는 북쪽에서 (r+1)번째에 있는 줄의 서쪽에서 (c+1)번째 칸을 가리킨다.
# 처음에 빈 칸은 전부 청소되지 않은 상태이다.

# d가
# 0인 경우 북쪽,
# 1인 경우 동쪽,
# 2인 경우 남쪽,
# 3인 경우 서쪽을 바라보고 있는 것이다.

# 로봇 청소기는 다음과 같이 작동한다.

# 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 현재 칸의 주변
# 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 반시계 방향으로 90도 회전한다.
# 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 1번으로 돌아간다.

# 문제 예시
# 11 10
# 7 4 0
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 0 1 1 0 0 0 0 1
# 1 0 1 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 v v 0 1 1 0 1
# 1 0 0 v v 0 1 1 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1


def get_count_cleaned_block(r: int, c: int, d: int, map: list[list[int]]):
    N = len(map)
    M = len(map[0])
    cur_r = r
    cur_c = c
    cur_d = d
    #  d =  0 1 2 3
    #       북 동 남 서
    d_r = [-1, 0, 1, 0]
    d_c = [0, 1, 0, -1]

    count = 0

    while True:
        if map[cur_r][cur_c] == 0:
            map[cur_r][cur_c] = 2
            count += 1

        # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        is_near_all_cleaned = True
        dir_now = cur_d  # 현재 방향 정보 담고, 아래에서 반시계방향으로 탐색
        for _ in range(4):
            dir_now = (dir_now - 1) % 4
            next_r = cur_r + d_r[dir_now]
            next_c = cur_c + d_c[dir_now]
            if 0 <= next_r < N and 0 <= next_c < M:
                if map[next_r][next_c] == 0:  # 청소되지않은칸이 있다면
                    is_near_all_cleaned = False
                    cur_r = next_r
                    cur_c = next_c
                    cur_d = dir_now
                    break

        # 주변 청소되지않은 칸이 있는경우 continue로 while 문부터 다시시작
        if is_near_all_cleaned == False:
            continue
        # 주변 청소되지않은 칸이 없는경우 : 현재 방향 유지 하면서 후진
        # 후진할 방향
        r_to_back = d_r[(cur_d - 2) % 4]
        c_to_back = d_c[(cur_d - 2) % 4]
        back_r = cur_r + r_to_back
        back_c = cur_c + c_to_back

        # 후진 범위 체크 추가 (맵을 벗어나면 종료)
        if not (0 <= back_r < N and 0 <= back_c < M) or map[back_r][back_c] == 1:
            break  # 벽이면 작동 종료

        cur_r = back_r
        cur_c = back_c

    return count


current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print("정답 = 57 / 현재 풀이 값 = ", get_count_cleaned_block(7, 4, 0, current_room_map))

current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(
    "정답 = 29 / 현재 풀이 값 = ", get_count_cleaned_block(6, 3, 1, current_room_map2)
)

current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(
    "정답 = 33 / 현재 풀이 값 = ", get_count_cleaned_block(7, 4, 1, current_room_map3)
)

current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(
    "정답 = 25 / 현재 풀이 값 = ", get_count_cleaned_block(6, 2, 0, current_room_map4)
)


# +alpha
# 좌표가 주어졌을때 방향제어방법
# 위 문제처럼 dr, dc 처럼 방향별 배열을 인덱스 기준으로 맞춰 제어할 수도 있지만,
# 벡터(튜플) 형태로 저장 후 제어도 가능하다.
#
# *** 방향을 (row 변화량, col 변화량) 튜플로 저장 ***
# DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
#
#  *** 방향을 딕셔너리로 정의 ***
# DIRECTION_MAP = {
#     "N": (-1, 0),
#     "E": (0, 1),
#     "S": (1, 0),
#     "W": (0, -1),
# }
