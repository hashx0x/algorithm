#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int a, int d, vector<bool> included)
{
    int answer = 0;
    int includedLength = included.size();
    cout << "includedLength" << includedLength << endl;

    for (int i = 0; i < includedLength; i++)
    {
        if (included[i])
        {
            cout << "i : " << i << endl;
            cout << "included[i] : " << included[i] << endl;
            answer += a + i * d;
        }
    }

    return answer;
}

int main()
{
    int a = 3; // 첫째 항
    int d = 4; // 공차

    // included를 std::vector로 정의
    std::vector<bool> included = {true, false, false, true, true};

    // solution 함수 호출
    int result = solution(a, d, included);

    // 결과 출력
    std::cout << "Result: " << result << std::endl;

    return 0;
}
