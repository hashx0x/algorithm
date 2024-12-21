# 백준 1439

# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# 예를 들어 S=0001100 일 때,
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


# 풀이
# 001100 -> 00 | 11 | 00 변화지점에 주목, 처음 숫자와 마지막 숫자가 같은지, 다른지...
# 1011001 -> 1 | 0 | 11 | 00 | 1 -> 변화지점 4개, 처음 숫자 = 마지막 숫자, 최소 수 2번 n/2
# 10110010 -> 1 | 0 | 11 | 00 | 1 | 0 -> 변화지점 5개 처음 숫자 != 마지막 숫자, 최소 수 3번, (n + 1)/2

# 1 | 0 | 1 | 0 | 1  0
## 처음 숫자 = 마지막 숫자면 변화지점 무조건 짝수개 => 총 구간수는 홀수개, 처음 숫자가 하나 더 많음
## 처음 숫자 != 마지막 숫자면 변화지점 무조건 홀수개 => 0,1 이 같은 구간 수 만큼 나뉘어짐

# 내가 알아야 할것 -> 처음 숫자, 나중숫자 , 몇번 바뀌었나

# input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    start: int = string[0]  
    end: int = string[-1]
    current: int = string[0]
    the_number_of_change: int = 0
    
    for char in string:
        if(char == current):
            continue
        else:
            the_number_of_change += 1
            current = char
    
    if(start == end):
        return int(the_number_of_change / 2) # 처음 = 마지막, 나눠진 공간은 change + 1
    else:
        return int((the_number_of_change + 1)/2)
    
   


print("1번")
print(f"답: 1, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one("011110")}")
print(f"답: 0, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one("11111")}")
print(f"답: 1, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one("00000001")}")
print(f"답: 4, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one("11001100110011000001")}")
print(f"답: 2, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one("11101101")}")

# another solution
# 0 -> 1 순간 0으로 뒤집는다 : 전체를 0 으로
# 1 -> 0 순간 1로 뒤집는다 : 전체를 1로

def find_count_to_turn_out_to_all_zero_or_all_one2(string:str):
    count_from_one_to_zero: int = 0
    count_from_zero_to_one: int = 0
    
    # 시작점에 따라 카운트 하나씩 추가
    if(string[0] == "0"): # 시작점이 0일 경우
        count_from_zero_to_one += 1 # 0을 1로 바꾸는 카운트를 하나 더 세야함
    elif(string[0] == "1"):
        count_from_one_to_zero += 1 # 1을 0으로 바꾸는 카운트를 하나 더 세야함
        
    for idx in range(len(string) - 1):
        if(string[idx] != string[idx + 1]):
            if string[idx + 1] == "1":
                count_from_one_to_zero += 1
            if string[idx + 1] == "0":
                count_from_zero_to_one += 1
                
    
    return min(count_from_zero_to_one, count_from_one_to_zero)
    
    
    
print("2번")
print(f"답: 1, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one2("011110")}")
print(f"답: 0, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one2("11111")}")
print(f"답: 1, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one2("00000001")}")
print(f"답: 4, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one2("11001100110011000001")}")
print(f"답: 2, 현재 : {find_count_to_turn_out_to_all_zero_or_all_one2("11101101")}")