# 백준 구슬탈출2
# link : https://www.acmicpc.net/problem/13460
# 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음,
# 빨간 구슬을 구멍을 통해 빼내는 게임이다.

# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다.
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
# 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고,
# 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다.
# 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

# 각각의 동작에서 공은 동시에 움직인다.
# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

# ******** 입력 ************
# 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다.
# 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
# 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
# '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
# 'O'는 구멍의 위치를 의미한다.
# 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다.
# 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

# ******** 출력 ************
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다.
# 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

# *******생각의 흐름*******
# 수형도 + 최단 라운드 => BFS
# 일단 red, blue 의 초기 좌표를 찾는다
# 움직이려는 방향으로 치우친 쪽을 먼저 움직인다
# 같은 선상에 있을땐 각각 움직인다.(순서 상관없음.)
# 움직였을때 B 가 먼저 hole 에 빠지는 경우는 넘긴다.
# R 가 먼저 hole 에 빠져도, B가 따라서 hole 에 빠지면 제외한다. > round 그대로, 다시 탐색
# round 가 10 이상인 경우 -1 반환
# 한 round 는 상하좌우 모두 탐색하는것, 다음 깊이(level)로 나아갈때 round 증가
# 중복되는 좌표라면 방문처리

# *********핵심 idea*********
# 해당 문제는 방향에 따라, 탐색시 만나는 것 (".", "#", "O") 들에 따라 이미 분기가 들어간다.
# 이럴때 누가 먼저 움직여야할지 순서까지 생각한다면 분기가 더 늘어난다.
# 따라서 단순화시킬 필요가 있다.
# 만약 같은 컬럼 에서 위 아래로 움직여야한다면, 더 위쪽에 있는걸 움직여야한다.
# 이걸 단순화 시키면 일단 # 또는 O 를 만날때까지 계속 움직이고, 그와 동시에 몇칸 움직였는지 카운팅을 한 후
# 두 물체의 좌표가 겹칠 때, 카운팅이 더 많은쪽을 해당 방향의 반대 방향으로 한칸 옮겨놓으면 된다.
# 이런 방법으로 분기처리를 좀 더 단순화 시킬 수 있다.

from collections import deque


def get_init_pos(n, m, game_map: list[list[int]]):
    red_init = []
    blue_init = []

    for i in range(0, n):
        for j in range(0, m):
            if game_map[i][j] == "R":
                red_init = [i, j]
            elif game_map[i][j] == "B":
                blue_init = [i, j]
    return {"red": tuple(red_init), "blue": tuple(blue_init)}


# data = {"round": 1, "red": (3, 1), "blue": (1, 3), "hole": (3, 2)}


# 이동은 next pos 가 "#" 이거나 cur_pos 가 "O" 인 지점에서 멈춰야한다
def move_marble(pos: tuple[int], dir: tuple[int], game_map):
    pos_r, pos_c = pos
    count = 0
    while True:
        cur_val = game_map[pos_r][pos_c]
        next_pos_r = pos_r + dir[0]
        next_pos_c = pos_c + dir[1]
        next_val = game_map[next_pos_r][next_pos_c]
        if cur_val == "O" or next_val == "#":
            break
        else:
            pos_r += dir[0]
            pos_c += dir[1]
            count += 1
    return (pos_r, pos_c, count)


def count_to_escape_red_marble(game_map: list[list[int]]):
    # 각 축 방향벡터배열 -> 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    n = len(game_map)
    m = len(game_map[0])
    round = 1

    init_pos = get_init_pos(n, m, game_map)

    red_init = init_pos["red"]
    blue_init = init_pos["blue"]

    # q에 넣을 data set 세팅
    data = {"round": round, "red": red_init, "blue": blue_init}

    # 방문처리 (red_r, red_c, blue_r, blue_c) 로 이루어진 set 사용
    visited = set()
    visited.add((red_init[0], red_init[1], blue_init[0], blue_init[1]))

    q = deque([data])

    while q:
        # 탐색시작
        popped = q.popleft()  # 현재

        round = popped["round"]
        if round > 10:
            return -1

        for i in range(4):
            next_red_r, next_red_c, red_count = move_marble(popped["red"], (dr[i], dc[i]), game_map)
            next_blue_r, next_blue_c, blue_count = move_marble(
                popped["blue"], (dr[i], dc[i]), game_map
            )

            # 넘기는경우
            if game_map[next_blue_r][next_blue_c] == "O":
                continue

            # 끝난 경우
            if game_map[next_red_r][next_red_c] == "O":
                return round

            # 겹치는 경우
            if next_red_r == next_blue_r and next_red_c == next_blue_c:
                # red가 더 많이 움직인경우 해당 반대방향으로 이동
                if red_count > blue_count:
                    next_red_r = next_red_r + (-dr[i])
                    next_red_c = next_red_c + (-dc[i])

                else:
                    next_blue_r = next_blue_r + (-dr[i])
                    next_blue_c = next_blue_c + (-dc[i])

            # 아직 방문처리 되지 않았다면 큐에넣고 계속 탐색
            if (next_red_r, next_red_c, next_blue_r, next_blue_c) not in visited:
                q.append(
                    {
                        "round": round + 1,
                        "red": (next_red_r, next_red_c),
                        "blue": (next_blue_r, next_blue_c),
                    }
                )
                visited.add((next_red_r, next_red_c, next_blue_r, next_blue_c))
    # 위 while loop 에서도 끝나지 않으면 못푸는 문제 return -1
    return -1


right_answer = [1, 5, 5, -1, 1, 7, -1]

test_cases = [
    [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", "B", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", "R", "O", ".", "#"],
        ["#", "#", "#", "#", "#"],
    ],
    [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "R", "B", "#"],
        ["#", ".", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", ".", "#"],
        ["#", "O", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#"],
    ],
    [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", "R", "#", "B", "#"],
        ["#", ".", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", ".", "#"],
        ["#", "O", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#"],
    ],
    [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "R", "#", ".", ".", ".", "#", "#", "B", "#"],
        ["#", ".", ".", ".", "#", ".", "#", "#", ".", "#"],
        ["#", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", ".", ".", "#"],
        ["#", ".", ".", ".", "#", ".", "O", "#", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ],
    [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", "R", ".", "O", ".", "B", "#"],
        ["#", "#", "#", "#", "#", "#", "#"],
    ],
    [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "R", "#", ".", ".", ".", "#", "#", "B", "#"],
        ["#", ".", ".", ".", "#", ".", "#", "#", ".", "#"],
        ["#", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", "#", ".", ".", ".", "#"],
        ["#", "O", ".", ".", "#", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ],
    [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ],
]


for i, case in enumerate(test_cases):
    print(f"정답 : {right_answer[i]}, 현재 답 : {count_to_escape_red_marble(case)}")
