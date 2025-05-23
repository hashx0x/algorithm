# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/60058
# 카카오에 신입 개발자로 입사한 콘은 선배 개발자로부터 개발역량 강화를 위해
# 다른 개발자가 작성한 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다.
# 소스를 컴파일하여 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
# 수정해야 할 소스 파일이 너무 많아서 고민하던 콘은 소스 코드에 작성된 모든 괄호를 뽑아서
# 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.

# 용어의 정의
# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
# 예를 들어, "(()))("와 같은 문자열은 균형잡힌 괄호 문자열 이지만 올바른 괄호 문자열은 아닙니다.
# 반면에 "(())()"와 같은 문자열은 균형잡힌 괄호 문자열 이면서 동시에 올바른 괄호 문자열 입니다.

# '(' 와 ')' 로만 이루어진 문자열 w가 균형잡힌 괄호 문자열 이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

# 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로 변환한 결과를 반환하시오.

# '(', ')' 개수 같다면 균형잡힌 괄호 문자열
# '(' ')' 의 위치와 짝이 맞다면 올바른 괄호 문자열
# 균형잡힌 문자열 w -> u(균형, 분리불가능) + v(균형, 빈 가능)
# if u가 올바른 -> v에 대해서 계속 진행
# if not u 올바른 ->

# u = (())   v = )( -> vu = )(, vv = ""  new = "(" + "" + ")" +


# '(' 와 ')' 를 구별해야한다.
#  ** u는 더이상 분리할수없는 균형잡힌 괄호 -> 길이가 두개짜리다(X), 짝수개이다,
# )))((( 도 더 이상 분리될수없는 균형잡힌 문자열, () 균형잡힌문자열, )( 균형잡힌문자열 -> 개수만 바로 맞춰지는순간 균형잡힌문자열
# ()  ))((() ->


def check_correct_parenthesis(w: str):
    stack = []  # 여기엔 '(' 만 들어간다.

    for char in w:
        if char == ")":
            if not stack:
                return False
            else:
                stack.pop()
                continue
        else:  # if char == '('
            stack.append(char)

    return not stack


def reverse_parens_direction(w: str):
    answer = ""
    for char in w:
        if char == "(":
            answer += ")"
        else:
            answer += "("
    return answer


def convert_to_correct_parenthesis(w: str):
    # 빈 문자열 반환
    if w == "":
        return ""

    # 올바른 문자열인지 확인하는 부분 필요
    if check_correct_parenthesis(w):
        return w

    # w를 u + v 로 분리하는 부분 필요
    l_parens_count: int = 0
    r_parens_count: int = 0
    u = ""
    v = ""
    for i in range(0, len(w)):
        if w[i] == "(":
            l_parens_count += 1

        else:
            r_parens_count += 1

        if l_parens_count == r_parens_count:
            u = w[: i + 1]
            v = w[i + 1 :]
            break

    # u가 올바른 문자열일 경우 v에 대해서 다시 재귀 -> 함수 재호출
    if check_correct_parenthesis(u):
        return u + convert_to_correct_parenthesis(v)
        # return convert_to_correct_parenthesis(v)

    # u가 올바른 문자열이 아닌 경우 new 연산
    else:
        # 파이썬 문자열 slicing str[start:end:step]
        # *** 파이썬에서 문자열을 슬라이싱 시 start, end는  방향까지 신경써야한다.
        # 맨앞, 맨뒤 제거 후 역순으로 읽는다 => string[-2:0:-1]
        # print(f"u[-2:0:-1] : {u[-2:0:-1]}")
        return (
            "("
            + convert_to_correct_parenthesis(v)
            + ")"
            + reverse_parens_direction(u[1:-1])
        )


print(
    f"입력값 = '(()())()',  정답 = '(()())()', 현재풀이값 = {convert_to_correct_parenthesis('(()())()')}, {'(()())()' == convert_to_correct_parenthesis('(()())()')} ",
)

print(
    f"입력값 = ')(',  정답 = '()', 현재풀이값 = {convert_to_correct_parenthesis(')(')}, {convert_to_correct_parenthesis(')(') == '()'}",
)

print(
    f"입력값 = '()))((()',  정답 = '()(())()', 현재풀이값 = {convert_to_correct_parenthesis('()))((()')}, {convert_to_correct_parenthesis('()))((()') == '()(())()'}",
)


# 세번째 예제 처리과정
# 1 : u = ()     v = ))((()
# 2:             u =  ) )( (         v = ()
# 3:             return (())()
