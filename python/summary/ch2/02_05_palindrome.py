input = "abcba"

count = 0
# recursive
def is_palindrome_sol_1(string):
    global count
    count += 1
    # print(f"count : {count}")
    if len(string) == 0:
        return True
    elif (string[0] != string[-1]):
        # print(f"string[0] : {string[0]}")
        # print(f"string[0] : {string[-1]}")
        return False
    elif string[0] == string[-1]:
        # print(f"string[0] : {string[0]}")
        # print(f"string[0] : {string[-1]}")
        return is_palindrome_sol_1(string[1:-1])

    return True


# for loop
def is_palindrome_sol_2(string):
    n = len(string)
    
    for i in range(n): # i: 0 ~ (n-1)
        if string[i] != string[n-1-i]:
            return False
    return True


print(f"sol1 answer : {is_palindrome_sol_1("abcba")}")
print(f"sol1 answer : {is_palindrome_sol_1("summuus")}")
print(f"sol1 answer : {is_palindrome_sol_1("xabbay")}")
print(f"sol1 answer : {is_palindrome_sol_1("comwwtmoc")}")
print(f"sol1 answer : {is_palindrome_sol_1("comwwmoc")}")







print(f"sol2 answer : {is_palindrome_sol_2("abcba")}")