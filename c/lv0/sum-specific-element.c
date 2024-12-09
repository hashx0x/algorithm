#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/*
등차수열의 특정한 항만 더하기
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는
solution 함수를 작성해 주세요.
included_len은 배열 included의 길이입니다.
*/

// 3, 4, [true, false, false, true, true] => 37
// 3 7 11 15 19 23
// 3 + 15 + 19 = 37

int solution(int a, int d, bool included[], size_t included_len)
{
    int answer = 0;
    // included 배열 확인 후 a에 d를 계속 더해주면서 반복진행, included_len 만큼
    for (int idx = 0; idx < (int)included_len; idx++)
    {
        if (included[idx] == true)
        {
            answer += a;
        }
        a += d;
    }

    // sol2
    // for (int i = 0; i < included_len; i++)
    // {
    //     if (included[i])
    //         answer += a + d * i; 등차수열 일반항
    // }

    return answer;
}

int main()
{
    int a = 3;
    int d = 4;
    bool included[] = {true, false, false, true, true};
    size_t included_len = sizeof(included) / sizeof(included[0]);

    int result = solution(a, d, included, included_len); // 함수 호출
    printf("Result: %d\n", result);

    return 0;
}