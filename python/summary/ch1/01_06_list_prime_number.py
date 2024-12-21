# 백준 1929
# number 이하의 소수 리스트 반환
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

input = 20


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


# More
# 과연 효율적인가?
# 2,3으로 나누어 떨어지지 않았는데 6으로 나누어 떨어지는가?
# 소인수분해를 생각해본다면, 모든 숫자는 소수의 거듭제곱으로 표현 가능 -> 소수로만 나누어떨어지는지 확인하면 된다.
# 또한 n = a * b 라고하면 a <= root(n), b<=root(n) 이므로 root(n) 보다 작은 지점까지만 탐색하면된다.


def improved_list_prime_number(number):
    prime_number:list[int] = []
    
    for target in range(2, number + 1):
        is_prime: bool = True # flag
        for prime_n in prime_number: # target이 소수로만 나누어 떨어지는 지 확인만 하면된다.
            # root(n) 보다 큰 범위 일 경우 break
            if(prime_n * prime_n > target):
                break
            # 소수로 나누어 떨어진다면
            if(target % prime_n == 0):
                is_prime = False
                break
        
        if(is_prime):
            prime_number.append(target)
    
    return prime_number