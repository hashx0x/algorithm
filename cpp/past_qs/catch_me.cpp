#include <deque>
#include <set>
#include <string>

#include "../util.h"

#define P_MAX 200000

using namespace std;

int catch_me(int cony, int brown) {
  int sec = 0;
  if (cony == brown) {
    return 0;
  }

  // queue 생성
  deque<int> queue;
  queue.push_back(brown);

  // 방문처리용 배열
  set<pair<int, int>> visited;  // include <set> 필요

  while (true) {
    // 시간 진행
    sec++;

    // 이번 round cony의 위치
    cony += sec;

    // cony의 범위 확인
    if (cony > P_MAX) return -1;

    // queue에 한번에 담을 배열
    vector<int> next_target;

    while (!queue.empty()) {
      int past_brown = queue.front();
      queue.pop_front();

      // 브라운이 이동할 수 있는 3가지
      int cur_1 = past_brown + 1;
      int cur_2 = past_brown - 1;
      int cur_3 = past_brown * 2;

      // 배열
      int candidates[3] = {cur_1, cur_2, cur_3};

      for (int cur : candidates) {
        if ((cur >= 0 && cur <= P_MAX) && (cony == cur)) {
          return sec;
        }

        // pair 만들기
        pair<int, int> state = make_pair(cur, sec);

        // 아직 방문처리되지않은
        if (visited.find(state) == visited.end()) {
          visited.insert(state);
          next_target.push_back(cur);
        }
      }
    }

    for (auto next : next_target) {
      queue.push_back(next);
    }
  }
}

int main() {
  int result = catch_me(11, 2);

  cout << "result: " << result << endl;

  return 0;
}