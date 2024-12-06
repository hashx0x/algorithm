#include <iostream>
#include <string>

using namespace std;

string solution(string code) {
  int mode = 0;
  int codeLength = code.size();
  string answer;
  cout << "mode : " << mode << "\n"
       << "codeLength : " << codeLength << "\n"
       << "answer : " << answer << endl;

  for (int idx = 0; idx < codeLength; ++idx) {
    if (code[idx] == '1') {
      mode = 1 - mode;
      continue;
    }
    if (mode == 0 && (idx & 1) == 0) {
      answer += code[idx];
    } else if (mode == 1 && (idx & 1) == 1) {
      answer += code[idx];
    }
  }
  cout << answer << endl;
  return answer;
}

int main() {
  string result = solution("abc1abc1abc");
  cout << result << endl;
  return 0;
}