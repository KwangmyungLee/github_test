


# count = int(input())

# for _ in range(count):
#     a, b = map(int, input().split())
#     print (a+b)



''' [Question 8393] John got a bad mark in math. The teacher gave him another task. John is to write a program which computes the sum of integers from 1 to n. If he manages to present a correct program, the bad mark will be cancelled.
Write a program which:
reads the number n from the standard input,
computes the sum of integers from 1 to n,
writes the answer to the standard output.
The first and only line of the standard input contains one integer n (1 ≤ n ≤ 10 000).
One integer is to be written to the standard output. This integer should be the sum of integers from 1 to n.
'''
# n = int(input())
# result = 0

# for i in range(1, n+1):
#     result += i
# print(result)


''' [Question 15552] '''
# import sys
# n = int(sys.stdin.readline())

# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     print (a+b)


''' [Question 2741]'''
# import sys
# n = int(sys.stdin.readline())

# for i in range(1, n+1):
#     print(i)

''' [Question 2742]'''
# import sys
# n = int(sys.stdin.readline())

# for i in range(n, 0,-1):
#     print(i)

'''[Question 11021] '''
# import sys
# n = int(sys.stdin.readline())
# for i in range(1, n+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print("Case #{}:".format(i),a+b)

'''[Question 11022] '''
# import sys
# n = int(sys.stdin.readline())
# for i in range(1, n+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print("Case #{}:".format(i), a, "+", b, "=", a+b)

'''[Question 2438] '''
# import sys
# n = int(sys.stdin.readline())

# for i in range(1, n+1):
#     print("*"*i)


'''[Question 2439] '''
# import sys
# n = int(sys.stdin.readline())

# for i in range(1, n+1):
#     c = n - i
#     print(" "*c + "*"*i)


'''[Question 10871] '''
# import sys
# n, x = map(int, sys.stdin.readline().split())
# element = list(map(int, sys.stdin.readline().split()))

# for i in range(n):
#     if element[i] < x:
#         print(element[i], end=" ")


'''[Question 10952] '''
# import sys

# a = 1
# b = 1

# while a != 0 and b != 0:
#     a, b = map(int, sys.stdin.readline().split())
#     if a==0 and b ==0:
#         break
#     print(a+b)



