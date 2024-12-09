def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    count_table = [0 for _ in range(len(alphabet_array))]; # 배열 초기화
    
    index_a = ord('a')
    max_index = 0
    
    for char in string: # 배열을 순회하면서 'a', 'b', ...
        if not char.isalpha(): # alphabet 아니면 다음 진행
            continue;
        
        index = ord(char) - index_a; #ord 함수 이용해 알파벳 아스키코드를 인덱스화 'a' -> 0 // 'b' -> 1
        print(f"char : {char}")
        print(f"index: {index}")
        
        count_table[index] += 1 # qoduf
        
        print(f"updated count_table_index : {count_table[index]}")
        print(f"max index : {max_index}")
        
        # 저장 후 현재 최대 값인 인덱스보다 그 수가 클 경우 max_index 갱신
        if count_table[index] > count_table[max_index]:
            print(f"updated index : {index}")
            print(f"count_table_index : {count_table[index]}")
            max_index = index
    
    print(count_table)
    print(f"max_index : {max_index}")
    print(f"index_a : {index_a}")
    
    
    
    return  chr(max_index + index_a)

def find_max_num(array):
    max_number = array[0];
    for number in array:
        # if max_number is None:
        #     max_number = number
        
        if number > max_number:
            max_number = number
        
    return max_number


# 문자열 확인
# print("a".isalpha())    # True
# print("1".isalpha())    # False
# s = "abcdefg"
# print(s[0].isalpha())   # True

# 알파벳 빈도수
# [0] => 'a';

# print(ord('a') - ord('a'));
# ord(문자) => ascii code
# chr(숫자) => ascii code 상 숫자의 값  (ord 역연산)

# 배열선언
# arr = [0] * 10  # 길이 10의 배열, 모든 값이 0
# arr = ['x'] * 5  # 길이 5의 배열, 모든 값이 'x'

# arr = [i for i in range(10)]  # 0부터 9까지의 숫자로 초기화
# arr = [i**2 for i in range(10)]  # 제곱값으로 초기화
# arr = ['value' for _ in range(5)]  # 'value'로 채워진 길이 5의 배열



print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))


#풀이1
# 알파벳별로 string을 순회
# string 을 순회하면서 카운팅