/**
 * 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다.
 * 예를 들면 다음과 같습니다.
 * 12 ⊕ 3 = 123
 * 3 ⊕ 12 = 312
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;
int circleplus(int a, int b) { return stoi(to_string(a) + to_string(b)); }

int solution(int a, int b) {
  int resultOfCirclePlus = circleplus(a, b);

  int multiply2ab = 2 * a * b;

  int answer = max(resultOfCirclePlus, multiply2ab);

  return answer;
}

int main() {
  int a = 12;
  int b = 3;

  int answer = solution(a, b);

  cout << "answer is : " << answer << endl;
}