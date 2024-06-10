def factorialNumber(n):
 if n==1:
    return 1
 else:
    return n * factorialNumber(n-1)

n=3
if n<0:
    print("enter a positive number")
elif n==0:
    print("1")
else:
    print(factorialNumber(n))


