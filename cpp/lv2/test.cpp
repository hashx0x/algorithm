#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

#include "../util.h"

using namespace std;

int main() {
  // unordered_map 선언
  unordered_map<string, vector<string>> umap;

  // 요소 삽입
  umap["fruit"] = {"apple", "banana", "cherry"};
  umap["vegetables"] = {"carrot", "broccoli"};

  // 요소 검색
  auto it = umap.find("fruit");
  printContainer(it->second);

  // if (it != umap.end()) {
  //   cout << "Found key 'fruit' with values: ";
  //   for (const auto& fruit : it->second) {
  //     cout << fruit << " ";
  //   }
  //   cout << endl;
  // } else {
  //   cout << "Key 'fruit' not found." << endl;
  // }

  // // 찾지 못한 경우
  // it = umap.find("meat");
  // if (it != umap.end()) {
  //   cout << "Found key 'meat'" << endl;
  // } else {
  //   cout << "Key 'meat' not found." << endl;
  // }

  // // 전체 요소 순회
  // for (auto it = umap.begin(); it != umap.end(); ++it) {
  //   cout << it->first << ": ";
  //   for (const auto& item : it->second) {
  //     cout << item << " ";
  //   }
  //   cout << endl;
  // }

  return 0;
}