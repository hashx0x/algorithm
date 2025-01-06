finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] # 길이 16
# 배열은 정렬이 되어있어야함.

# r1 : cur_idx = 16, arr[cur_idx] > target
# r2 : cur_idx = 16 // 2 arr[cur_idx] = 9 < target
# r3 : cur_idx = cur_idx

# 최소인덱스와 최대 인덱스를 한 라운드마다 조정해야한다.
# 인덱스 변수를 두개 두어 조작한다.

# 처음 1 ~ N
# 1회탐색 : 1 ~ N/2
# 2회탐색 : 1 ~ N/2^2
# 3회탐색 : 1 ~ N/2^3
# k회탐색 : 1 ~ N/2^k
# 1개가 남는다면
# 1 = N/2^k ==> k = log_2(N) ==> O(log_2(N))

def is_existing_target_number_binary(target, array):
    index_max = len(array) - 1
    index_min = 0
    index_mid = (index_max - index_min) // 2
    
    if target == array[index_min] or target == array[index_max]:
        return True
    
        
    while (index_min <= index_max):
        if target < array[index_mid]:
            index_max = index_mid - 1
        elif target > array[index_mid]:
            index_min = index_mid + 1
        
        index_mid 
        
    
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)