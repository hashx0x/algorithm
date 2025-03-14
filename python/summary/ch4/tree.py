#     8      Level 0
#   6   3    Level 1
#  4 2 5     Level 2  # -> 이진 트리 && 완전 이진 트리

# 트리 ->> 배열로 표현 (완전이진트리인 경우에만 해당, 규칙성보유)
# 트리 구현시 편의성을 위해 0번째 인덱스 사용 X
# [None] 으로 시작

#       8      Level 0 -> [None, 8] 첫번째 레벨 추가
#     6   3    Level 1 -> [None, 8, 6, 3] 두번째 레벨 추가
#    4 2 5     Level 2 -> [None, 8, 6, 3, 4, 2, 5] 세번째 레벨 추가

# => [None, 8, 6, 3, 4, 2, 5]
# 역으로 배열로 트리 파악이 가능

#   0    1  2  3  4  5  6
# [None, 8, 6, 3, 4, 2, 5]

#  level 0 / 1   / 2
#   0  / 1 /2  3 /4  5  6
# [None, 8, 6, 3, 4, 2, 5]

# 1. 현재 인덱스 * 2 -> 왼쪽 자식의 인덱스
# 2. 현재 인덱스 * 2 + 1 -> 오른쪽 자식의 인덱스 1 * 2 + 1 =3
# 3. 현재 인덱스 // 2 -> 부모의 인덱스

# 예) 1번째 인덱스인 8의 왼쪽 자식은 6, 오른쪽 자식은 3
# 따라서 1 * 2 = 2번째 인덱스 = 6
# 따라서 1 * 2 + 1 = 3번째 인덱스 = 3
# 부모를 찾아보면, 3 // 2 = 1번째 인덱스 8 => 부모의 인덱스이다.

# 다시 배열을 보면
# [None, 8, 6, 3, 4, 2, 5] 는
# 8 밑에 6, 3 이 있고, 6, 3 밑에 4, 2, 5가 있는 완전 이진 트리임을 알수있다.
