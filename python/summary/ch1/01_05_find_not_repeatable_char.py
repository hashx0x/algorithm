input = "abadabac"

def find_not_repeating_first_character(string):
    count_table: list[int] = count_occurence_char(string) # O(n)
    
    answer: str = '_'
    
    for char in string: #O(n)
        # abadabac
        # [4 2 1 1 0 0 0 0 ... ]
        idx: int = ord(char) - ord('a')
        if(count_table[idx] % 2 == 1):
            answer = char
            break
        
    return answer
    
    


def count_occurence_char(string):
    count_table: list[int] = [0]*(ord('z') - ord('a'))
    answer: str | None
    
    for char in string:
        if not char.isalpha():
            continue;
        
        index = ord(char) - ord('a')
        count_table[index] += 1
    
    return count_table


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

# Take
# 한 반복문 내에서 한번에 여러 로직을 처리하기 위해 반복문을 한번 더 돌리면서 O(n^2)
# 을 만드는것보단 여러반복문으로 쪼개는게 더 낫다.