# min && 람다함수 사용법 lambda (매개변수) : 결과값


# 예제

counter: dict[int, dict[str, int]] = {}

min_1: int = min(
    counter,
    key=lambda k: (
        sum(counter[k].values())
        if sum(counter[k].values()) != len(counter[k])
        else float("inf")
    ),
)

min_2: int = min(
    counter,
    key=lambda k: (
        sum(counter[k].values())
        if any(v > 1 for v in counter[k].values())
        else float("inf")
    ),
)


# min함수 부가설명
# max, min 은 iterable 객체에서 기준값을 토대로 최소 또는 최대값을 가진 것을 반환
# key= 인자는 비교의 기준값을 지정해주는것
# 여기서는 sum(counter[k].values()) 사용. 단 해당 count 가 1개이면 의미가 없으므로 인자중 최소 1개는 2이상인 키값들중에서만 비교 시작
# float("inf")는 양의 무한대값을 나타내며 어떤 가산 숫자 보다 큰값을 나타낸다. 10000 < float("inf") 는 True -> 최소값 탐색에 유용
# 반대로 최대값 탐색에서 float("-inf") 도 사용가능하다 (음의 무한대)

# min_1
# 초기값이 1이므로, sum값이 키값과 같을 경우 해당 결과물은 float("inf") 를 반환함으로써 최소값 대상에서 제외

# min_2
# any 함수 사용
# any(iterable) 은 iterable 에 대해서 단 하나라도 만족하는 결과값을 반환한다.
# 아래 if any(v > 1 for v in counter[k].values()) else float("inf") 에서
# v > 1 for v in counter[k].values() 은 제네레이터 표현식으로 한번에 하나씩 값을 생성하는 이터레이터를 만들어낸다.
