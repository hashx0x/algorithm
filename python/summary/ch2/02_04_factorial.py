def factorial(n):
    if n <= 1: 
        return 1
    facto = n * factorial(n-1)
     
    return facto
    
    


print(factorial(5))