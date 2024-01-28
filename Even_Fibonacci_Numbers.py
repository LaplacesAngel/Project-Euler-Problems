#Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms


#try 2

# a, b = 1,2
# n = 4000000
# sum = 0

# while b <= n:
#     a, b = b, a+b
#     if a % 2 == 0:
#         sum += a
#         print(f"Sum is", sum, "a is", a, 'b is', b)


#make a function out of it
        
def findThesumOfevenFibsunder(n):
    a, b = 1,2
    sum = 0
    while b <= n:
        a, b = b, a + b
        if a % 2 == 0:
            sum += a
    print(sum)



findThesumOfevenFibsunder(4000000)

























#try 1
# a,b = 1,2
# n=4000000
# sum1 = 0
# sum2 = 0
# arr = []

# while b <= n:
#     a,b = b, a+b
#     arr.append(a)
#     if a % 2 == 0:
#         sum1 +=a

# print(arr)
# for x in arr:
#     if x % 2 == 0:
#         sum2 += x

# print(sum1, sum2)
