# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/67257
# 문제 설명
# IT 벤처 회사를 운영하고 있는 라이언은 매년 사내 해커톤 대회를 개최하여 우승자에게 상금을 지급하고 있습니다.
# 이번 대회에서는 우승자에게 지급되는 상금을 이전 대회와는 다르게 다음과 같은 방식으로 결정하려고 합니다.
# 해커톤 대회에 참가하는 모든 참가자들에게는
# 숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식이 전달되며,
# 참가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여
# 만들 수 있는 가장 큰 숫자를 제출하는 것입니다.
# 단, 연산자의 우선순위를 새로 정의할 때,
# 같은 순위의 연산자는 없어야 합니다. 즉, + > - > * 또는 - > * > + 등과 같이
# 연산자 우선순위를 정의할 수 있으나 +,* > - 또는 * > +,-처럼
# 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없습니다.
# 수식에 포함된 연산자가 2개라면 정의할 수 있는 연산자 우선순위 조합은 2! = 2가지이며,
# 연산자가 3개라면 3! = 6가지 조합이 가능합니다.
# 만약 계산된 결과가 음수라면
# 해당 숫자의 절댓값으로 변환하여 제출하며 제출한 숫자가 가장 큰 참가자를 우승자로 선정하며,
# 우승자가 제출한 숫자를 우승상금으로 지급하게 됩니다.

# 예를 들어, 참가자 중 네오가 아래와 같은 수식을 전달받았다고 가정합니다.

# "100-200*300-500+20"

# 일반적으로 수학 및 전산학에서 약속된 연산자 우선순위에 따르면
# 더하기와 빼기는 서로 동등하며 곱하기는 더하기, 빼기에 비해 우선순위가 높아
# * > +,- 로 우선순위가 정의되어 있습니다.
# 대회 규칙에 따라 + > - > * 또는 - > * > + 등과 같이 연산자 우선순위를 정의할 수 있으나
# +,* > - 또는 * > +,- 처럼 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없습니다.
# 수식에 연산자가 3개 주어졌으므로 가능한 연산자 우선순위 조합은 3! = 6가지이며,
# 그 중 + > - > * 로 연산자 우선순위를 정한다면 결괏값은 22,000원이 됩니다.
# 반면에 * > + > - 로 연산자 우선순위를 정한다면 수식의 결괏값은 -60,420 이지만,
# 규칙에 따라 우승 시 상금은 절댓값인 60,420원이 됩니다.

# 참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때,
# 우승 시 받을 수 있는 가장 큰 상금 금액을 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# expression은 길이가 3 이상 100 이하인 문자열입니다.
# expression은 공백문자, 괄호문자 없이 오로지 숫자와
# 3가지의 연산자(+, -, *) 만으로 이루어진
# 올바른 중위표기법(연산의 두 대상 사이에 연산기호를 사용하는 방식)으로 표현된 연산식입니다.
# 잘못된 연산식은 입력으로 주어지지 않습니다.
# 즉, "402+-561*"처럼 잘못된 수식은 올바른 중위표기법이 아니므로 주어지지 않습니다.
# expression의 피연산자(operand)는 0 이상 999 이하의 숫자입니다.
# 즉, "100-2145*458+12"처럼 999를 초과하는 피연산자가 포함된 수식은 입력으로 주어지지 않습니다.
# "-56+100"처럼 피연산자가 음수인 수식도 입력으로 주어지지 않습니다.
# expression은 적어도 1개 이상의 연산자를 포함하고 있습니다.
# 연산자 우선순위를 어떻게 적용하더라도,
# expression의 중간 계산값과 최종 결괏값은 절댓값이 2^63 - 1 이하가 되도록 입력이 주어집니다.
# 같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높습니다.

# 풀이방법
# 일단 주어진 string 형태의 표현식을 연산자와 피연산자로 구분하는게 첫번째 작업
# 연산자의 우선순위 가짓수를 구하는게 두번째 작업 -> 순열로 구한다.

import itertools


def operate(num1, num2, operator):
    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    else:
        return num1 - num2


def solution(expression):
    answer = 0

    # 등장한 연산자간의 우선순위를 정하기 위한 연산자 set(중복이 불필요하기 때문에 set을 선택)
    op_set = set()

    expression_arr = []
    number_str = ""

    # expression에서 연산자와 피연산자 분리과정
    for char in expression:
        # 연산자 중 하나라면 현재 쌓인 피연산자 string을 expression_arr에 추가,
        # expression_arr에 연산자 스트링도 따로 추가한다.
        # op_set(연산자 세트)에 연산자를 추가한다.
        if char == "*" or char == "+" or char == "-":
            expression_arr.append(int(number_str))
            expression_arr.append(char)
            op_set.add(char)
            number_str = ""
        else:
            number_str += char
    # 마지막 피연산자
    expression_arr.append(int(number_str))

    # 연산자 우선순위 순열로 구하기
    permutation = list(itertools.permutations(op_set))

    # 우선순위 각 종류에따라 결과값 계산
    for perm in permutation:
        # temp 에 현재 연산자식 복사
        temp_expression_arr = expression_arr[:]

        # 각 경우 내 연산자 순서로 계산 시작
        for operator in perm:
            # 연산식에 해당 오퍼레이터가 있을때까지,
            while operator in temp_expression_arr:
                # 연산자의 인덱스 찾기
                op_idx = temp_expression_arr.index(operator)

                # 연산결과 계산
                result = operate(
                    # 연산자 앞 수
                    temp_expression_arr[op_idx - 1],
                    # 연산자 뒤 수
                    temp_expression_arr[op_idx + 1],
                    # 연산자
                    operator,
                )
                # 기존 연산자의 앞 수 인덱스 값을 result로 치환
                temp_expression_arr[op_idx - 1] = result
                # 연산식 갱신
                temp_expression_arr = (
                    temp_expression_arr[:op_idx] + temp_expression_arr[op_idx + 2 :]
                )

        # 루프를 돌면서 answer 갱신 작업
        answer = max(answer, abs(temp_expression_arr[0]))

    return answer


# 100 - 200 * 300 - 500 + 20   , *
# [100, '-', 200, '*', 300, '-', 500, '+']

test_case = [
    {"in": "100-200*300-500+20", "out": 60420},
    {
        "in": "50*6-3*2",
        "out": 300,
    },
]

# 1. 01:00:03


for i in range(len(test_case)):
    if i == 0:
        print(f"정답 : {test_case[i]["out"]}, 현재출력 : {solution(test_case[i]["in"])}")
    # print(f"정답 : {test_case[i]["out"]}, 현재출력 : {solution(test_case[i]["in"])}")
