import time
start_time = time.time()

a: str = 'aaa'
print(a)



# integer 양의정수, 음의정수, 0
# 실수형 : 변수에 소수점을 붙인수 => 실수형 변수로 처리
# 지수 표현 가능 : e or E 
a = 1e9
print(a)

b = 5.
c = -13.7
print(b)
print(c)

# /: 결과 실수형,  %: 나머지 연산,  //: 몫 연산자, **: 거듭제곱

# 리스트
# append, 
a = [0] * 10
print(a)

a= [1,2,3,4,5]
print(a)
print(a[-1])

array = [i for i in range(10)]
print(array)


array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(2,10)]
print(array)

# 2차원배열 초기화
array = [[0]*3 for _ in range(4)]
print(array)

array[1][1] = 5
print(array)


# array = [[0]*m]*n 은 리스트 내 각 리스트가 모두 같은 객체로 인식됨
array = [[0]*3]*4
print(array)
array[1][1] = 5
print(array)

# 반복내 변수값 무시할때 _ 사용

# reverse, insert, count, remove
a = [4,3,2,1]

a.reverse()
print(a)

a.insert(2,3)
print("index 2에 3 추가", a)

print("값이 3인 데이터 개수", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제", a)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]

print("remove_list 에 포함되지 않은 값", result)

remove_set_2 = [3,5]

result2 = [i for i in a if i not in remove_set_2]

print(result2)


# 튜플: 한번 선언된 값 변경 불가, 
# 서로 다른 성질의 데이터 묶어서

#데이터의 나열을 해싱의 키값으로 사용해야할때

# 리스트보다 메모리를 효율적으로 사용해야할때



# dictionary
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)



# 집합자료형
data = set([1,1,2,2,3,4,4,5])
print(data)

data = {1,1,2,2,3,4,4,5}
print(data)

# 합집합, 교집합, 차집합
a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a | b)
print(a & b)
print(a - b)

# add, update (add 여러개), remove


# 기본입출력
# 5
# 65 90 75 34 99

# n = int(input())
# print(n)

# array = list(map(int, input().split()))
# print(array)




# end_time = time.time()
# print("time: ", end_time - start_time)

