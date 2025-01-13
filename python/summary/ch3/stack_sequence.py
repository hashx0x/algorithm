# 코드 설계시 처음이 아닌 n번째 상황에서 생각해보자. 점화식 구조를 파악하는게 중요
def stack_sequence(n, sequence):
    base_sequence_stack = [i for i in range(n, 0, -1)]
    print(f"base_seq : {base_sequence_stack}")
    stack = []
    answer = []
    sequence_idx = 0

    while True:
        if len(stack) == 0:  # 맨처음
            cur_num = base_sequence_stack.pop()
            print(f"cur num : {cur_num}")
            stack.append(cur_num)
            answer.append("+")
        elif stack[-1] == sequence[sequence_idx]:  # target을 찾았을 경우
            stack.pop()
            answer.append("-")
            sequence_idx += 1
            if sequence_idx == n:
                break
        else:
            # No 조건
            if sequence_idx >= n:
                return "NO"
            if len(base_sequence_stack) == 0:
                return "NO"
            cur_num = base_sequence_stack.pop()
            print(f"cur num : {cur_num}")
            stack.append(cur_num)
            answer.append("+")
        # print(f"stack : {stack}")
        # print(f"stack[-1] : {stack[-1]}")
        # print(f"sequence[sequence_idx] : {sequence[sequence_idx]}")

    return answer


# sequence = list()
# n = int(input())
# for _ in range(n):
#     sequence.append(int(input()))
# stack_sequence(n, sequence)

print(
    f"정답 : ['+', '+', '+', '+', '-', '-', '+', '+', '-', '+', '+', '-', '-', '-', '-', '-'], 현재값 : {stack_sequence(8, [4,3,6,8,7,5,2,1])}"
)

print(f"정답 : 'NO', 현재값 : {stack_sequence(5, [1,2,5,3,4])}")
