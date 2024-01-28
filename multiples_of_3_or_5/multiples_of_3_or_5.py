#TODO If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000.


sum = 0
for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x

print(sum)

#success!

import os
if os.path.exists("Even_Fibonacci_Numbers.py"):
    os.remove("Even_Fibonacci_Numbers.py")
else:
    print("File not found")

f = open("Even_Fibonacci_Numbers.py", "w") \
    .write("#Each new term in the Fibonacci sequence is generated by adding the previous two terms. \n\
#By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89\n\
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms")