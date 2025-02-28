# https://www.acmicpc.net/problem/17837

# 재현이는 주변을 살펴보던 중 체스판과 말을 이용해서 새로운 게임을 만들기로 했다.
# 새로운 게임은 크기가 N×N인 체스판에서 진행되고, 사용하는 말의 개수는 K개이다.
# 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.

# 게임은 체스판 위에 말 K개를 놓고 시작한다.
# 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다.
# 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.

# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다.
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다.
# 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다.
# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.

# A번 말이 이동하려는 칸이
#   흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
#       A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
#       예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한 후에는 D, E, A, B, C가 된다.
#   빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
#       A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
#       A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.
#   파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
#       방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
# 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.

# 첫째 줄에 체스판의 크기 N, 말의 개수 K가 주어진다.
# 둘째 줄부터 N개의 줄에 체스판의 정보가 주어진다.
# 체스판의 정보는 정수로 이루어져 있고, 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.

# 다음 K개의 줄에 말의 정보가 1번 말부터 순서대로 주어진다.
# 말의 정보는 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향이다.
# 행과 열의 번호는 1부터 시작하고,
# 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.

#   1 2 3 4
# 1
# 2
# 3
# 4

# 1 : (0,1)
# 2:  (0,-1)
# 3:  (-1,0)
# 4: (1,0)

# 파이썬 타입 관련
# NestedDict = dict[str, int | list[int]]
# MyDictType = dict[tuple[int, int], NestedDict]
# ChessMapInfo: MyDictType = {}
# # ColorType = "WHITE" | "RED" | "BLUE" << 이건 안된다
# Number_Color_Map: dict[int, callable] = {0: "WHITE", 1: "RED", 2: "BLUE"}
# Color_Fucntion_Map: dict[str, callable] = {"WHITE": 1, "RED": 2, "BLUE": 3}


# 같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다.

from collections import deque


# 패딩을 해줌으로써 주어진 1-based 좌표계를 0-based 좌표계(리스트) 처럼 사용할수있다.
def pad_with_twos(matrix):
    n = len(matrix)  # 원래 배열의 크기 (n x n)
    # 상단 패딩 행 추가
    padded = [[2] * (n + 2)]
    # 각 행의 좌우에 2를 추가하여 새로운 행을 구성
    for row in matrix:
        padded.append([2] + row + [2])
    # 하단 패딩 행 추가
    padded.append([2] * (n + 2))
    return padded


# 방향 바꾸기
def switch_direction(number: int):
    # if number == 1:
    #     return 2
    # elif number == 2:
    #     return 1
    # elif number == 3:
    #     return 4
    # elif number == 4:
    #     return 3

    if number % 2 == 1:
        return number + 1
    else:
        return number - 1


def new_game_2(n: int, k: int, chess_map: list[list[int]], piece_info: list[list[int]]):
    # 방향 벡터 매핑 table -> 방향종류가 지금처럼 4개정도일떈 x방향 배열, y방향 배열로 나눠서 관리하기도 한다.
    direction_mapping = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

    # 막다른곳 파란색(2)으로 패딩
    chess_map = pad_with_twos(chess_map)

    round = 0
    # 몇번말인지 고려 필요하므로 hashtable로 관리
    piece_table = {i + 1: piece_info[i] for i in range(0, len(piece_info))}

    map_table: dict[tuple[int, int], list[int]] = {
        (piece_table[piece][0], piece_table[piece][1]): [piece] for piece in piece_table
    }

    # 1번말부터 순서대로 실행 queue에 넣는다.

    # 턴 반복 loop
    while True:
        for key, lst in map_table.items():
            if len(lst) >= 4:
                print(f"키 {key}에 해당하는 리스트의 길이가 4가 되었습니다: {lst}")
                return round

        round += 1
        if round > 1000:
            return -1

        q = deque(list(piece_table.keys()))  # 1, 2, 3, 4, ...

        # 턴 내 체스말 이동 loop
        while q:
            # 큐에서 꺼낸 해당 말 번호
            popped = q.popleft()
            # 해당 말 번호의 정보 조회
            chess_piece_info = piece_table[popped]
            # 현재 위치 저장
            cur_loc = [chess_piece_info[0], chess_piece_info[1]]
            # 방향정보 가져오기
            direction_num = chess_piece_info[-1]
            # 방향조회
            direction = direction_mapping[direction_num]

            # next loc 계산
            next_loc = [chess_piece_info[0] + direction[0], chess_piece_info[1] + direction[1]]

            # 다음 위치 color값 가져오기 ->
            next_loc_color_val = chess_map[next_loc[0]][next_loc[1]]

            # 방향이 바뀌는 다음 갈 곳이 파란색일 경우 부터 처리
            if next_loc_color_val == 2:
                changed_direction_number = switch_direction(direction_num)
                # piece table에 바뀐 방향 정보 업데이트
                piece_table[popped][-1] = changed_direction_number

                direction = direction_mapping[changed_direction_number]
                next_loc = [
                    chess_piece_info[0] + direction[0],
                    chess_piece_info[1] + direction[1],
                ]
                next_loc_color_val = chess_map[next_loc[0]][next_loc[1]]
                if next_loc_color_val == 2:
                    continue

            indexof_piece_num_in_cur_loc = map_table[tuple(cur_loc)].index(popped)
            # 남을 말들
            remainings = map_table[tuple(cur_loc)][:indexof_piece_num_in_cur_loc]

            leavings = (
                map_table[tuple(cur_loc)][indexof_piece_num_in_cur_loc:]
                if next_loc_color_val == 0
                else map_table[tuple(cur_loc)][indexof_piece_num_in_cur_loc:][::-1]
            )
            # ****** 위 삼항연산자를 이렇게도 쓸수있다 ******
            # if next_loc_color_val == 0:  # WHITE
            #     leavings = map_table[tuple(cur_loc)][indexof_piece_num_in_cur_loc:]
            # elif next_loc_color_val == 1:  # RED
            #     leavings = map_table[tuple(cur_loc)][indexof_piece_num_in_cur_loc:][::-1]

            # 배열갱신
            map_table[tuple(cur_loc)] = remainings
            # leaving 에 대해 for loop 순회하면서 piece_table 좌표 갱신
            for leaving in leavings:
                # 기존정보
                prev = piece_table[leaving]
                piece_table[leaving] = [next_loc[0], next_loc[1], prev[-1]]

            # 다음 갈곳에 추가
            if tuple(next_loc) in map_table:
                map_table[tuple(next_loc)].extend(leavings)
            else:
                map_table[tuple(next_loc)] = []
                map_table[tuple(next_loc)].extend(leavings)

            if len(map_table[tuple(next_loc)]) >= 4:
                return round


n_case_1 = 4
k_case_1 = 4
chess_map_case_1 = [[0, 0, 2, 0], [0, 0, 1, 0], [0, 0, 1, 2], [0, 2, 0, 0]]
piece_info_case_1 = [[2, 1, 1], [3, 2, 3], [2, 2, 1], [4, 1, 2]]

n_case_2 = 4
k_case_2 = 4
chess_map_case_2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
piece_info_case_2 = [[1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1]]

n_case_3 = 4
k_case_3 = 4
chess_map_case_3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
piece_info_case_3 = [[1, 1, 1], [1, 2, 1], [1, 3, 1], [2, 4, 3]]

n_case_4 = 4
k_case_4 = 4
chess_map_case_4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
piece_info_case_4 = [[1, 1, 1], [1, 2, 1], [1, 3, 1], [3, 3, 3]]

n_case_5 = 6
k_case_5 = 10
chess_map_case_5 = [
    [0, 1, 2, 0, 1, 1],
    [1, 2, 0, 1, 1, 0],
    [2, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 2],
    [2, 0, 1, 2, 0, 1],
    [0, 2, 1, 0, 2, 1],
]
piece_info_case_5 = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 4],
    [4, 4, 1],
    [5, 5, 3],
    [6, 6, 2],
    [1, 6, 3],
    [6, 1, 2],
    [2, 4, 3],
    [4, 2, 1],
]
print(
    f"정답 : -1, 현재풀이값 : {new_game_2(n=n_case_1, k=k_case_1, chess_map=chess_map_case_1, piece_info=piece_info_case_1)}"
)
print(
    f"정답 : 1, 현재풀이값 : {new_game_2(n=n_case_2, k=k_case_2, chess_map=chess_map_case_2, piece_info=piece_info_case_2)}"
)
print(
    f"정답 : 1, 현재풀이값 : {new_game_2(n=n_case_3, k=k_case_3, chess_map=chess_map_case_3, piece_info=piece_info_case_3)}"
)
print(
    f"정답 : 2, 현재풀이값 : {new_game_2(n=n_case_4, k=k_case_4, chess_map=chess_map_case_4, piece_info=piece_info_case_4)}"
)
print(
    f"정답 : 7, 현재풀이값 : {new_game_2(n=n_case_5, k=k_case_5, chess_map=chess_map_case_5, piece_info=piece_info_case_5)}"
)
