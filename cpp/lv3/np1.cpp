#include <iostream>
#include <string>
#include <vector>

#include "../util.h"

using namespace std;

int solution(int coin, vector<int> cards) {
  int answer = 0;
  int cardsLength = cards.size();

  vector<int> startCards(cards.begin(), cards.begin() + cardsLength / 3);

  printContainer(cards);
  printContainer(startCards);

  return answer;
}

int main() {}