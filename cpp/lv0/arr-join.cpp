#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

string solution(vector<string> arr) {
  string answer = "";

  answer = accumulate(arr.begin(), arr.end(), string(""));

  // for (int i =0; i < arr.size(); i++) {
  //       answer += arr[i];
  //   }

  cout << answer << endl;

  return answer;
}

int main() {
  string answer = solution({"a", "b", "c"});
  return 0;
}