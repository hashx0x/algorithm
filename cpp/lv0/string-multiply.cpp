#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int k) {
  string answer = "";
  for (auto i = 0; i < k; i++) {
    answer += my_string;
  }

  return answer;
}

int main() {
  string answer = solution("abc", 3);

  cout << answer << endl;
  return 0;
}