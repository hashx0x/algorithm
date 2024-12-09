input = 20

# number 이하의 소수 리스트 반환

def list_prime_number(number):
    answer: list[int] = []
    for i in range(2, number+1):
        print(f"outer f i: {i}")
        print(f"outer f isPrimeNumber : {check_is_prime_num(i)}")
        if(check_is_prime_num(i) == True):
            answer.append(i)
        
    
    return answer

# 소수는 인수가 자기자신 또는 1 (인수는 나눴을때 나머지가 0)
def check_is_prime_num(number):
    
    # n/2 까지만 인수인지 확인하면 끝
    last_checking_number = int(number / 2 if number % 2 == 0 else (number + 1) / 2)
    
    for i in range(1, last_checking_number + 1):
        # i 가 1이 아니면서, number를 i 로 나눴을때 나머지가 0인게 존재한다면 소수가 아니다
        if(i != 1  and number % i == 0):
            return False
        
    return True



result = list_prime_number(input)
print(result)