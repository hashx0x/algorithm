#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string str1, string str2) {
  string answer = "";

  for (int i = 0; i < str1.length(); i++) {
    answer += str1[i];
    answer += str2[i];
  }

  return answer;
}

int main() {
  //   str1	str2	result
  // "aaaaa"	"bbbbb"	"ababababab"

  string answer = solution("aaaaa", "bbbbb");

  cout << "answer : " << answer << endl;

  return 0;
}