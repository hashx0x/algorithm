#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

#include "../util.h"
using namespace std;

// 문제 설명
// 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서
// 출발합니다.

// 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항
// 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

// 제한사항
// 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
// 주어진 공항 수는 3개 이상 10,000개 이하입니다.
// tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는
// 의미입니다. 주어진 항공권은 모두 사용해야 합니다. 만일 가능한 경로가 2개
// 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다. 모든 도시를 방문할 수
// 없는 경우는 주어지지 않습니다.

// 입출력 예 tickets return
// [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
// ["ICN", "JFK", "HND", "IAD"]
// [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL",
// "ICN"],["ATL","SFO"]]
// 	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

vector<string> solution(vector<vector<string>> tickets) {
  unordered_map<string, vector<string>> ticketGraph;

  printContainer(ticketGraph);

  // graph 세팅
  for (vector<string> ticket : tickets) {
    ticketGraph[ticket[0]].push_back(ticket[1]);
  }

  cout << "ticket Graph: " << endl;
  printContainer(ticketGraph);

  for (auto& graph : ticketGraph) {
    sort(graph.second.begin(), graph.second.end(), greater<string>());
  }
  cout << "here" << endl;
  printContainer(ticketGraph);

  vector<string> answer;
  vector<string> stack;
  stack.push_back("ICN");

  while (stack.size() > 0) {
    string current = stack.back();

    if (!ticketGraph[current].empty()) {  // 아직 더 들어갈 곳이 있다면
      stack.push_back(ticketGraph[current].back());  // 스택에 요소추가
      ticketGraph[current].pop_back();               // 그래프에서는 pop
    } else {                      // 이 요소가 마지막이라면
      answer.push_back(current);  // answer에 요소추가
      stack.pop_back();
    }
  }

  reverse(answer.begin(), answer.end());

  return answer;
}

int main() {
   vector<vector<string>> tickets = {{"ICN", "SFO"},
                                    {"ICN", "ATL"},
                                    {"SFO", "ATL"},
                                    {"ATL", "ICN"},
                                    {"ATL", "SFO"}};

  vector<string> answer = solution(tickets);

  printContainer(answer);

  return 0;
}