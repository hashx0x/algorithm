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

int solution(int a, int b) {
  string aString = to_string(a);
  string bString = to_string(b);

  int answer1 = stoi(aString + bString);
  int answer2 = stoi(bString + aString);

  int answer = max(answer1, answer2);
  return answer;
}

int circleplus(int a, int b) { return stoi(to_string(a) + to_string(b)); }

int main() {
  int a = 9;
  int b = 91;

  int answer = solution(a, b);

  cout << answer << endl;
}