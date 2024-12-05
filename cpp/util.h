#ifndef UTIL_H
#define UTIL_H

#include <iostream>
#include <map>
#include <utility>  // for std::pair
#include <vector>

// Forward declarations of operator<<
template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p);

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec);

// Definitions of operator<<
template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
  os << "{" << p.first << ", " << p.second << "}";
  return os;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec) {
  os << "[";
  for (auto it = vec.cbegin(); it != vec.cend(); ++it) {
    os << *it;
    if (std::next(it) != vec.cend()) {
      os << ", ";
    }
  }
  os << "]";
  return os;
}

// Template function to print any container
template <typename Container>
void printContainer(const Container& container) {
  std::cout << "[";
  for (auto it = container.cbegin(); it != container.cend(); ++it) {
    std::cout << *it;
    if (std::next(it) != container.cend()) {
      std::cout << ", ";
    }
  }
  std::cout << "]" << std::endl;
}

#endif  // UTIL_H
