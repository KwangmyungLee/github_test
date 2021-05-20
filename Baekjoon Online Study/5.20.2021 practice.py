'''[Question 10952] '''
# import sys

# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         print(a+b)
#     except:
#         break


''' Fail [Question 1110] '''
# import sys
# copy = n = int(sys.stdin.readline())
# count = 0

# while True:
#     a = copy//10
#     b = copy%10
#     c = a+b
#     result = b*10 + c%10
#     count += 1
#     copy = result
#     if n == result:
#         break

# print(count)


# ''' [Question 10818] '''
# n = int(input())
# list_1 = list(map(int, input().split()))

# max = -10000000
# min = 10000000
# for i in range(n):
#     if list_1[i] > max:
#         max = list_1[i]
#     if list_1[i] < min:
#         min = list_1[i]

# print(min, max)


''' [Question 2562] '''
# list_1 = []
# for i in range(1, 10):
#     n = int(input())
#     list_1.append(n)

# max = 0
# index = 0
# for i in range(len(list_1)):
#     if list_1[i] > max:
#         max = list_1[i]
#         index = i+1

# print(max)
# print(index)

''' [Question 2577] '''
# a = int(input())
# b = int(input())
# c = int(input())

# n = str(a*b*c)

# for i in range(0,10):
#     print(n.count(str(i)))


''' [Question 3052] '''

result_1 = []
for _ in range (10):
    n = int(input())
    n = n%42
    result_1.append(n)
result_2 = set(result_1)
print(len(result_2))
    













