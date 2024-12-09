#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* code) {
  // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게
  // 변경해주세요.
  int codeLength = strlen(code);
  char* answer = (char*)malloc(
      codeLength);  // answer 의 길이는 절대 code의 길이를 넘을 수 없다.
  bool mode = 0;
  int answerCurrentMaxIdx = 0;

  for (int idx = 0; idx < codeLength; ++idx) {
    if (code[idx] == '1') {
      mode = 1 - mode;
      continue;
    }
    if (mode == 0 && (idx & 1) == 0) {
      answer[answerCurrentMaxIdx] = code[idx];
      answerCurrentMaxIdx++;
    } else if (mode == 1 && (idx & 1) == 1) {
      answer[answerCurrentMaxIdx] = code[idx];
      answerCurrentMaxIdx++;
    }
  }

  return answer;
}

int main() {
  char* result = solution("abc1abc1abc");
  printf("%s\n", result);
  free(result);
  return 0;
}