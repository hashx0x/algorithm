# 백준 치킨 배달
# 문제 링크 : https://www.acmicpc.net/problem/15686

# 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다.
# 도시의 칸은 (r, c)와 같은 형태로 나타내고,
# r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다.
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
# 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

# 예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.

# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2

# 0은 빈 칸, 1은 집, 2는 치킨집이다.

# (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2,
# (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다.
# 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

# (5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6,
# (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다.
# 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.

# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다.
# 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다.
# 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

# ********입력********
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

# ********출력********
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

# ********생각의 흐름********
# 치킨집 수 최대 13 -> 조합 최대 수는 13 C 6 -> 경우의 수가 크지않기 때문에 전수조사 가능
# 13 개중 m 개의 치킨집 선택 후 그 조합에 따른 치킨거리를 계산해야한다. ->


def combination(n: int, r: int):

    result = []
    stack = [{"data": [i], "next": i + 1} for i in range(n, 0, -1)]

    while stack:
        popped = stack.pop()

        cur_data, next = popped.values()

        if len(cur_data) == r:
            result.append(cur_data)
            continue

        # 거꾸로 stack에 넣어준다
        for i in range(n, next - 1, -1):
            stack.append({"data": cur_data + [i], "next": i + 1})

    return result


def get_house_and_chickens_pos(n, city_map):
    pos = {1: [], 2: []}

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                pos[1].append((i, j))
            elif city_map[i][j] == 2:
                pos[2].append((i, j))

    return pos


# 어느 한 집의 치킨거리
def get_chicken_dis(house_pos, chickens_pos_list):
    house_x, house_y = house_pos
    chicken_dis = float("inf")
    for i in range(len(chickens_pos_list)):
        x, y = chickens_pos_list[i]
        chicken_dis = min(chicken_dis, abs(x - house_x) + abs(y - house_y))

    return int(chicken_dis)


def chicken_delivery(n: int, m: int, city_map: list[list[int]]):
    houses_and_chickens_pos = get_house_and_chickens_pos(n, city_map)
    houses = houses_and_chickens_pos[1]
    chickens = houses_and_chickens_pos[2]

    combs = combination(len(chickens), m)

    city_chicken_dis = float("inf")

    # 모든 조합에 대해 치킨 거리를 계산해봐야함
    for comb in combs:
        # 해당 라운드의 치킨집들 조합
        chickens_pos_list = [chickens[comb_index - 1] for comb_index in comb]

        # 각 집에서부터 치킨집의 치킨거리 계산
        total_chicken_dis = 0
        for house in houses:
            sum += get_chicken_dis(house_pos=house, chickens_pos_list=chickens_pos_list)

        city_chicken_dis = min(city_chicken_dis, total_chicken_dis)

    return city_chicken_dis


# 입력값 (n x n 이차배열의 배열) << 1-based array 거리를 구하는 것이기 때문에 무시하고 0 -based 를 사용해도 되나?
# 테스트 입력값 (n, m, n x n 이차배열)
test_cases = [
    (
        5,
        3,
        [  # 예제 입력 1
            [0, 0, 1, 0, 0],
            [0, 0, 2, 0, 1],
            [0, 1, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 2],
        ],
    ),
    (
        5,
        2,
        [  # 예제 입력 2
            [0, 2, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [2, 0, 0, 1, 1],
            [2, 2, 0, 1, 2],
        ],
    ),
    (
        5,
        1,
        [  # 예제 입력 3
            [1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0],
        ],
    ),
    (
        5,
        1,
        [  # 예제 입력 4
            [1, 2, 0, 2, 1],
            [1, 2, 0, 2, 1],
            [1, 2, 0, 2, 1],
            [1, 2, 0, 2, 1],
            [1, 2, 0, 2, 1],
        ],
    ),
]

# 출력값 (정답 리스트)
right_answer = [5, 10, 11, 32]

# 테스트 실행
for i, (n, m, city_map) in enumerate(test_cases):
    # if i == 1:
    #     print(f"정답 : {right_answer[i]}, 현재 답 : {chicken_delivery(n, m, city_map)}")
    # else:
    #     continue
    print(f"정답 : {right_answer[i]}, 현재 답 : {chicken_delivery(n, m, city_map)}")
