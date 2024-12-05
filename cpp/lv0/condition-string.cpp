#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string ineq, string eq, int n, int m) {
  int answer = 0;
  if (ineq == ">" && eq == "=") {
    answer = n >= m;
  } else if (ineq == "<" && eq == "=") {
    answer = n <= m;
  } else if (ineq == ">" && eq == "!") {
    answer = n > m;
  } else {
    answer = n < m;
  }

  // 가독성?
  // return ineq == "<"? eq == "="? n<=m? 1:0 : n<m? 1:0 : eq == "="? n>=m ? 1:0
  // : n>m ?1:0;
  return answer;
}

int main() {
  // string ineq = "<";
  // string eq = "=";
  // int n = 20;
  // int m = 50;

  string ineq = ">";
  string eq = "!";
  int n = 41;
  int m = 78;

  int answer = solution(ineq, eq, n, m);

  cout << "answer : " << answer << endl;

  return 0;
}