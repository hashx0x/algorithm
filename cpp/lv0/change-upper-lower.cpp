#include <cctype>
#include <iostream>
#include <string>

using namespace std;

int main(void) {
  string str;
  cin >> str;

  string answer;

  for (char& s : str) {
    if (isupper(static_cast<unsigned char>(s)) == true) {
      s = towlower(static_cast<unsigned char>(s));
    } else {
      s = toupper(static_cast<unsigned char>(s));
    }
  }

  cout << str << endl;

  return 0;
}