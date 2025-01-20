# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

from collections import deque


def is_correct_parenthesis(string):
    q = deque(string)
    stack = []  # 스택엔 ( 만 들어간다

    while q:
        dequed = q.popleft()
        if dequed == ")":
            # 스택 길이 0 이면 False
            if len(stack) == 0:
                return False
            else:
                stack.pop()
                continue
            # 스택에 있으면 꺼내오기

            # 못꺼내오면 return False
        else:
            stack.append(dequed)
    if len(stack) != 0:
        return False
    return True


# 다듬은 버전
# 큐는 필요가없다 -> for loop 순회
# return not stack : 비어있으면 True
def is_correct_parenthesis_clean(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if not stack:  # 스택이 비어있을때
                return False
            stack.pop()  # () 맞추기

    return not stack  # 스택이 비었으면 True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis_clean("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_clean(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_clean("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_clean("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_clean("((())"))
