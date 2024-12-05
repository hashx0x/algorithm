#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {
  int overwrite_string_length = overwrite_string.length();
  cout << "overwrite_string_length : " << overwrite_string_length << endl;
  for (int i = 0; i < my_string.length(); i++) {
    if (i >= s && i < s + overwrite_string_length) {
      cout << "my_string[i] : " << my_string[i] << endl;
      cout << "overwrite_string[i - s] : " << overwrite_string[i - 2] << endl;
      my_string[i] = overwrite_string[i - s];
    }
  }

  string answer = my_string;

  cout << "changed_string : " << my_string << endl;
  return answer;
}

// #include <string>
// #include <vector>

// using namespace std;

// string solution(string my_string, string overwrite_string, int s) {
//     string answer = "";
//     answer = my_string.replace(s,overwrite_string.size(),overwrite_string);
//     return answer;
// }

int main() {
  // "He11oWor1d"	"lloWorl"	2	"HelloWorld"
  // "Program29b8UYP"	"merS123"	7	"ProgrammerS123"

  // string answer = solution("He11oWor1d", "lloWorl", 2);

  string answer = solution("Program29b8UYP", "merS123", 7);

  cout << answer << endl;
}