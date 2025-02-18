# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.

# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.

# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다

# 풀이
# 코니의 모든 위치는 초기값을 통해 모두 결정된다.
# 결국 브라운의 n번째 모든 위치를 다 파악해야된다. -> 수형도 기반 탐색을 진행해야함
# 1초 기준 모든 경우의 수를 탐색해봐야한다. -> 최소시간 구해야하므로 bfs
# 중간에 같은초에 같은 위치값을 탐색해야하는경우는 visited 처리


# test case
# cony = 11, brown = 2
# time :  0,  1,  2,  3,  4,  5
# cony : 11, 12, 14, 17, 21, 26
# brown:  2,  4,  8, 16, 24,

# C    C1 + n(n+1)/2    //// C1 + n(n+1)/2 + n+1 //// C1 + n(n+1)/2 + n+1 + n+2
# B -> (B+1), (B-1), 2B //// (B), (B+2), 2(B+1) // B+1, B-1, 2B
#           (홀  짝) 홀 or 짝   + 짝  +  홀
# 2B = C1 + n(n+1)/2 + n+1 + n+2


from collections import deque


def catch_me(cony: int, brown: int):
    P_MAX = 200000

    print(f"cony : {cony}")
    print(f"brown : {brown}")

    # 초설정
    sec: int = 0
    # 맨처음에 같을때 retunr 0
    if cony == brown:
        return 0

    # 다음 Round 탐색 대상 적재용 queue
    queue = deque()
    queue.append(brown)  # (position, time) 로 queue 에 추가

    # 방문처리용 배열
    visited_set: set[tuple[int, int]] = set()

    while True:
        # 시간의 흐름
        sec += 1

        # 이번 round cony의 위치
        cony += sec

        # 코니의 범위 확인 (단조증가이므로, 우측끝 값만 확인)
        if cony > P_MAX:
            return -1

        # queue에 담을 배열
        next_target: list[tuple[int, int]] = []

        # queue확인
        while queue:
            # 이전 round queue data
            past_brown = queue.popleft()
            print(f"cur bronw : {past_brown}")

            cur_1 = past_brown + 1
            cur_2 = past_brown - 1
            cur_3 = past_brown * 2

            for cur in [cur_1, cur_2, cur_3]:
                if (cur >= 0 and cur <= P_MAX) and cony == cur:
                    return sec

                # 아직 (cur, n) 이 조사되지 않은 상태라면
                if (cur, sec) not in visited_set:
                    visited_set.add((cur, sec))
                    next_target.append(cur)

            # if (cony == cur_1) or (cony == cur_2) or (cony == cur_3):
            #     return sec

            # next_target.extend([next1, next2, next3])

        queue.extend(next_target)


print(f"{catch_me(11, 2)}")


from collections import deque


def catch_cony_bfs(cony_start, brown_start):
    MAX_POS = 200000
    # 방문 여부를 (위치, 시각)으로 관리하는 딕셔너리(또는 2차원 배열)
    visited = set()  # 예: (pos, time)을 넣어서 체크

    # 시작 상태
    queue = deque()
    queue.append((brown_start, 0))  # (브라운 위치, 시각)
    visited.add((brown_start, 0))

    # 만약 애초에 브라운==코니 시작이면 0초
    if cony_start == brown_start:
        return 0

    # BFS
    while queue:
        brown_pos, t = queue.popleft()

        # 코니 위치(시각 t에)
        cony_pos = cony_start + t * (t + 1) // 2
        if cony_pos > MAX_POS:
            # 코니가 범위를 벗어났다면 잡을 수 없으므로 -1
            return -1

        # 만약 지금 시점에서 이미 브라운 == 코니?
        if brown_pos == cony_pos:
            return t

        # 브라운이 다음 초(t+1)에 갈 수 있는 위치들
        for next_pos in (brown_pos - 1, brown_pos + 1, brown_pos * 2):
            if 0 <= next_pos <= MAX_POS:
                # 다음 시각 = t+1
                next_time = t + 1
                # 그 시각에 코니 위치도 미리 구해 볼 수 있음
                # cony_next_pos = cony_start + next_time*(next_time+1)//2
                # 하지만 큐에 넣기 전에 일치 여부 확인해도 되고,
                # 보통은 큐에서 뺄 때 확인해도 괜찮음.

                # (next_pos, next_time)이 아직 미방문이면
                if (next_pos, next_time) not in visited:
                    visited.add((next_pos, next_time))
                    queue.append((next_pos, next_time))

    # 큐가 다 빌 때까지 못 찾으면 -1
    return -1


# 간단 테스트

print(catch_cony_bfs(11, 2))  # 5 나와야 함
print(catch_cony_bfs(10, 0))  # 다른 예시
