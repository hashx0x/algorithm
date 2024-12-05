#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
  cout << "here : " << endl;
  int answer = 0;

  if (n % 2 == 0) {
    for (int i = 0; i <= n; i += 2) {
      answer += i * i;
    }

  } else {
    for (int i = 1; i <= n; i += 2) {
      answer += i;
    }
  }
  cout << "here" << endl;

  return answer;
}

// int solution(int n) {
//     int answer = 0;
//     while(n>0)
//     {
//         answer += n%2==0 ? n*n : n;
//         n-=2;
//     }
//     return answer;
// }

int main() {
  int target = 10;

  int answer = solution(target);

  cout << "answer : " << answer << endl;
  return 0;
}