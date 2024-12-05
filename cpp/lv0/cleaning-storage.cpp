#include<iostream>  
#include <string>
#include <vector>

using namespace std;


template <typename T>
void printVector(const std::vector<T>& vec) {
    std::cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i];
        if (i != vec.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}
// string solution(vector<string> storage, vector<int> num) {
    // int num_item = 0;
    // vector<string> clean_storage(storage.size());
    // vector<int> clean_num(num.size());
    
    // for(int i=0; i<storage.size(); i++){
    //     int clean_idx = -1;
    //     for(int j=0; j<num_item; j++){
    //         if(storage[i] == clean_storage[j]){
    //             clean_idx = j;
    //             break;
    //         }
    //     }
    //     if(clean_idx == -1){
    //         clean_storage[num_item] = to_string(num[i]);
    //         clean_num[num_item] = num[i];
    //         num_item += 1;
    //     }
    //     else{
    //         clean_num[clean_idx] += num[i];
    //     }
    // }
    
    
    
    // int num_max = -1;
    // string answer = "";
    // for(int i=0; i<num_item; i++){
    //     if(clean_num[i] > num_max){
    //         num_max = clean_num[i];
    //         answer = clean_storage[i];
    //     }
    // }
    // return answer;
// }


string solution(vector<string> storage, vector<int> num) {  
    // storage: {"mirror", "net", "mirror", "net", "bottle"} , num : {4, 1, 4, 1, 5}    
    
    vector<string> clean_storage; // 정리용 storage
    vector<int> clean_storage_count; // 정리용 storage count

    int maxCountIdx = 0;

    for(int i = 0; i<storage.size(); i++ ) {        
        // 찾기위한 값 >>   -1: clean_storage 에 없는 경우, 아니면 기존 인덱스 할당
        int currentProductIdx = -1;

        // clean_storage 내에 이미 저장되었는지 탐색
        for(int j = 0; j < clean_storage.size(); j++) {
          if(clean_storage[j] == storage[i]) {
            currentProductIdx = j;
          }          
        };
        cout << "currendProductIdx : " << currentProductIdx << endl;

        if(currentProductIdx != -1) { // 이미 clean_storage 에 있는경우 >> 기존 값 업데이트
          // cout << storage[i] << endl;

          clean_storage_count[currentProductIdx] += num[i];
          if (clean_storage_count[currentProductIdx] > clean_storage_count[maxCountIdx]) maxCountIdx = currentProductIdx;

          continue;
        }
        // clean_storage에 없는 경우 >> 추가
        clean_storage.push_back(storage[i]);
        clean_storage_count.push_back(num[i]);

        if(num[i] > clean_storage_count[maxCountIdx] ) maxCountIdx = clean_storage.size() -1;    
    };



    string answer = clean_storage[maxCountIdx];

    cout<< "maxCountIdx : " << maxCountIdx <<endl;

    cout << "clean_storage : ";
    printVector(clean_storage);
    cout << endl;

    cout << "clean_storage_count : ";
    printVector(clean_storage_count);
    cout << endl;    

    return answer;
}

int main() {
  vector<string> storage = {"mirror", "net", "mirror", "net", "bottle"};
  vector<int> num = {4, 1, 4, 1, 5};

  string answer = solution(storage, num);

  cout << "answewr: " << answer << endl;

  return 0;
}