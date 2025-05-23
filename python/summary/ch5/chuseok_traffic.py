# 추석트래픽 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17676
# 이번 추석에도 시스템 장애가 없는 명절을 보내고 싶은 어피치는 서버를 증설해야 할지 고민이다.
# 장애 대비용 서버 증설 여부를 결정하기 위해
# 작년 추석 기간인 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량을 계산해보기로 했다.
# 초당 최대 처리량은 요청의 응답 완료 여부에 관계없이
# 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.

# 입력 형식
# solution 함수에 전달되는 lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열로 되어 있으며,
# ***각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분되어 있다.***
# 응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함하여
# 고정 길이 2016-09-15 hh:mm:ss.sss 형식으로 되어 있다.
# 처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며
# 뒤에는 초 단위를 의미하는 s로 끝난다.
# 예를 들어,
# 로그 문자열 2016-09-15 03:10:33.020 0.011s은
# "2016년 9월 15일 오전 3시 10분 33.010초"부터 "2016년 9월 15일 오전 3시 10분 33.020초"까지
# "0.011초" 동안 처리된 요청을 의미한다. (처리시간은 시작시간과 끝시간을 포함)
# 서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 0.001 ≦ T ≦ 3.000이다.
# lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬되어 있다.
# 출력 형식
# solution 함수에서는 로그 데이터 lines 배열에 대해 초당 최대 처리량을 리턴한다.

# 예제2
# 입력: [
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]
# 출력: 2

# 설명: 처리시간은 시작시간과 끝시간을 포함하므로
# 첫 번째 로그는 01:00:02.003 ~ 01:00:04.002에서 2초 동안 처리되었으며,
# 두 번째 로그는 01:00:05.001 ~ 01:00:07.000에서 2초 동안 처리된다.
# 따라서, 첫 번째 로그가 끝나는 시점과 두 번째 로그가 시작하는 시점의 구간인
# 01:00:04.002 ~ 01:00:05.001 1초 동안 최대 2개가 된다.

# 예제3
# 입력: [
# "2016-09-15 20:59:57.421 0.351s",     20:59:57:071 ~ 20:59:57:421
# "2016-09-15 20:59:58.233 1.181s",     20:59:57:053 ~ 20:59:58.233
# "2016-09-15 20:59:58.299 0.8s",       20:59:57.500 ~ 20:59:58.299
# "2016-09-15 20:59:58.688 1.041s",     20:59:57.648 ~ 20:59:58.688
# "2016-09-15 20:59:59.591 1.412s",     20:59:58.180 ~ 20:59:59.591
# "2016-09-15 21:00:00.464 1.466s",     21:59:59.999 ~ 21:00:00.464
# "2016-09-15 21:00:00.741 1.581s",     21:00:59.161 ~ 21:00:00.741
# "2016-09-15 21:00:00.748 2.31s",      21:00:58.439 ~ 21:00:00.748
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]

# 출력: 7

# 설명: 아래 타임라인 그림에서
# 빨간색으로 표시된 1초 각 구간의 처리량을 구해보면
# (1)은 4개,
# (2)는 7개,
# (3)는 2개임을 알 수 있다.
# 따라서 초당 최대 처리량은 7이 되며,
# 동일한 최대 처리량을 갖는 1초 구간은 여러 개 존재할 수 있으므로
# 이 문제에서는 구간이 아닌 개수만 출력한다.

# ********* 풀이 *********
# 최대인 지점 후보는
# 로그들의 딱 경계값이 1분 구간에 포함되는 지점이다.
# 해당 처리의 시작점과 끝점중 하나만 알면된다
# 문제에서 주어진게 끝점이므로,
# 끝점기준으로 [끝점,끝점+999ms] 되는 범위가 후보범위 -> 나머지 로그가 이 범위에 포함되는지 관찰
# 주어진 기준점이 시작점이라면, [시작점 -999ms, 시작점] 범위가 후보 범위이다.
# why?
# 중요한건 경계점이 포함될때 최댓값이 발생한다는것. 따라서 [끝점,끝점+999ms] 범위로 설정해야,
# 최대후보상태 (현재 끝점의 데이터를 포함한 상태) 라는 것.
# 주어진 점이 끝점일때, [끝점-999, 끝점] 범위를 후보범위로 잡을 경우. 최대가 아닐 수 있다.


def solution(lines):
    answer = 0
    timesets = []
    for line in lines:
        _, end_time_str, processing_time = line.split()
        hour, minute, second = end_time_str.split(":")

        # 시작, 끝 시간 계산
        end_time_ms = (int(hour) * 3600 + int(minute) * 60 + float(second)) * 1000
        start_time_ms = end_time_ms - float(processing_time.rstrip("s")) * 1000 + 1

        timesets.append((start_time_ms, end_time_ms))

    for timeset in timesets:

        # 1초구간 세팅
        _, candidate_end = timeset
        candidate_end_p_1 = candidate_end + 1000 - 1

        # 배열의 나머지 요소에 대해서 확인
        count = 0
        for timeset in timesets:

            start, end = timeset
            if not (end < candidate_end or candidate_end_p_1 < start):
                count += 1

        answer = max(answer, count)
        count = 0

    return answer


test_case = [
    {"in": ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"], "out": 2},
    {
        "in": [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s",
        ],
        "out": 7,
    },
    {"in": ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"], "out": 1},
]

# 1. 01:00:03


for i in range(len(test_case)):
    # if i == 1:
    #     print(f"정답 : {test_case[i]["out"]}, 현재출력 : {solution(test_case[i]["in"])}")
    print(f"정답 : {test_case[i]["out"]}, 현재출력 : {solution(test_case[i]["in"])}")
