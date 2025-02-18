# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현 (1은생략)

# 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현하는 알고리즘

# 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,

# 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있다

# 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법이다.

# 다른 예로, abcabcdede와 같은 경우,

# 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만,

# 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 된다.

# 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 된다.

# 압축할 문자열 input이 매개변수로 주어질 때,

# 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 string_compression 함수를 완성하라.

# * 문자열의 길이는 1 이상 1,000 이하입니다.
# * 문자열은 알파벳 소문자로만 이루어져 있습니다.
# 이 때, 문자열은 항상 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 입출력 예 #5 처럼 xababcdcdababcdcd 이 입력되어도,
# 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능합니다.
# 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

# 풀이 전 생각
# 자를수있는 최대길이 : length / 2
# count 세어서 compressed string에 합쳐준다 ***** 단 자른 요소가 연속된 경우일때만 *****
# 모두 탐색 후 가장 길이가 작은 compressed의 길이 return


def string_compression(input: str) -> int:
    if len(input) == 1:
        return 1

    cur_slice_number = 1
    limit_slice_number = len(input) // 2

    answer = len(input)

    while cur_slice_number <= limit_slice_number:

        prev: str = ""
        count: int = 0
        compressed: str = ""

        for i in range(0, len(input), cur_slice_number):
            # 맨 처음
            if compressed == "" and prev == "":
                prev = input[i : i + cur_slice_number]
                count += 1
                continue

            # 두번째부터
            cur = input[i : i + cur_slice_number]

            # 연속으로 같은 덩어리가 나온경우
            if cur == prev:
                count += 1
            # 더 이상 연속된 단위가 안나올 때 -> 누적된 prev값을 한번에 연산, cur 값은 아직 연산되지않는다
            else:
                # count 가 1보다 클 경우, count 까지 포함해서 compressed 에 추가
                if count > 1:
                    compressed += str(count) + prev
                # count가 1인 경우, 그대로 compressed에 추가
                else:
                    compressed += prev

                prev = cur
                count = 1
        # for loop 이 끝나고 남은 덩어리 처리
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        # answer 를 최소값으로 갱신
        answer = min(answer, len(compressed))
        cur_slice_number += 1
    return answer


print(
    f"input : ababcdcdababcdcd, answer : 9, current_ans : {string_compression("ababcdcdababcdcd")}",
)


print(
    f"input : abcabcdede, answer : 8, current_ans : {string_compression("abcabcdede")}",
)


# other solution
# splited 라는 배열에 기준 수만큼 자른 결과물들을 넣어두고,
# spllited를 순회하면서 연속된 값을 처리하면서, 압축결과물을 만들어준다.
# splited = [input[i:i+step] for i in range(0, len(input), step)]


def string_compression_2(input: str) -> int:
    input_length = len(input)
    answer = input_length
    for slice_size in range(1, (input_length // 2) + 1):
        slices = [input[i : i + slice_size] for i in range(0, input_length, slice_size)]

        compressed: str = ""
        count: int = 1
        for i in range(0, len(slices) - 1):
            cur, next = slices[i], slices[i + 1]

            if cur == next:
                count += 1
            else:
                if count == 1:
                    compressed += cur
                else:
                    compressed += f"{count}{cur}"

        # 남은 문자열 처리
        if count == 1:
            compressed += slices[-1]
        else:
            compressed += f"{count}{slices[-1]}"

        answer = min(answer, len(compressed))

    return answer


print(
    f"***solution 2***\n input : ababcdcdababcdcd, answer : 9, current_ans : {string_compression_2("ababcdcdababcdcd")}",
)
