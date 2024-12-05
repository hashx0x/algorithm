#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
  int time = 0;
  queue<int> bridge_queue;
  int current_truck_index = 0;
  int current_truck_weights_sum = 0;

  // 시간 재기 위해  queue 에 0의 개수를 bridge_length 만큼 세팅
  // why? 인덱스 한칸 = 1초 를 변수없이 세팅하기위해
  for (int i = 0; i < bridge_length; ++i) {
    bridge_queue.push(0);
  }

  // 현재 트럭 인덱스 가 트럭 배열 사이즈보다 작을때 까지
  while (bridge_queue.size() > 0) {
    time++;

    // queue 에서 하나 제거
    current_truck_weights_sum -= bridge_queue.front();
    bridge_queue.pop();

    // 현재 인덱스가 truck_weights 의 length 보다 작은 경우에만 진행
    if (current_truck_index < truck_weights.size()) {
      // queue weight 체크해서 들어갈수 있으면 push, 없으면 0 push
      if (current_truck_weights_sum + truck_weights[current_truck_index] <=
          weight) {
        // cout << "&&&&&&&&& time" << time << endl;
        // cout << "&&&&&&&&&" << truck_weights[current_truck_index] << endl;
        if (truck_weights[current_truck_index] == 0) {
          continue;
        }
        // 큐에 현재 인덱스 push
        bridge_queue.push(truck_weights[current_truck_index]);

        // 현재 다리 위 무게합에 추가
        current_truck_weights_sum += truck_weights[current_truck_index];

        // 인덱스 증가
        current_truck_index++;
      } else {
        // 큐에 0 push
        bridge_queue.push(0);
      }
    }
  }

  return time;
}

int main() {
  int bridge_length = 2;
  int weight = 10;
  vector<int> truck_weights = {7, 4, 5, 6};

  int result = solution(bridge_length, weight, truck_weights);

  cout << "result : " << result << endl;

  return 0;
}