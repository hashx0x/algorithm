#  특정노드 ~ 다른모든노드로 가는 최단경로 계산
#  음의간선이없을떄 정상동작
#  그리디알고리즘
#  매상황에서 가장 비용이적은노드선택
#  다이나믹프로그래밍

# 동작과정
# 1. 출발노드 설정
# 2. 최단거리 테이블 초기화
# 3. 방문하지 않은 노드중 최단거리 가장 짧은노드 선택
# 4. 해당 노드를 거쳐 다른노드로 가는 비용을 계산해 최단거리 테이블 갱신
# 5. 3,4번반복


# 예제
graph = {
    1: [(2,2), (3,5),(4,1)],
    2: [(3,3),(4,2)],
    3: [(2,3), (6,5)],
    4: [(3,3), (5,1)],
    5: [(3,1), (6,2)],
    6: []
}

import sys, typing;

input = sys.stdin.readline;
INF = int(1e9);
print(f'input : {input}');
print(f'input split : {input().split()}')
n, m = map(int, input().split());
print(n)
print(m)
# array = [1,2,3,4,5]
# map(int, a)

