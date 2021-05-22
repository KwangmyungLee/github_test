''' [Question 8958] 
Question
There is an objective test result such as “OOXXOXXOOO”. An ‘O’ means a correct answer of a problem and an ‘X’ means a wrong answer. The score of each problem of this test is calculated by itself and its just previous consecutive ‘O’s only when the answer is correct. For example, the score of the 10th problem is 3 that is obtained by itself and its two previous consecutive ‘O’s. 
Therefore, the score of “OOXXOXXOOO” is 10 which is calculated by “1+2+0+0+1+0+0+1+2+3”. 
You are to write a program calculating the scores of test results. 

input
Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case starts with a line containing a string composed by ‘O’ and ‘X’ and the length of the string is more than 0 and less than 80. There is no spaces between ‘O’ and ‘X’. 

output
Your program is to write to standard output. Print exactly one line for each test case. The line is to contain the score of the test case.'''

# n = int(input())

# for i in range(n):
#     case = input()
#     point = 0
#     accumul = 1
#     for i in range(len(case)):
#         if case[i] == "O":
#             point += accumul
#             accumul +=1
#         if case[i] == "X":
#             accumul = 1
        
#     print(point)


''' [Question 4344] 
question
It is said that 90% of frosh expect to be above average in their class. You are to provide a reality check.

input
The first line of standard input contains an integer C, the number of test cases. C data sets follow. Each data set begins with an integer, N, the number of people in the class (1 <= N <= 1000). N integers follow, separated by spaces, each giving the final grade (an integer between 0 and 100) of a student in the class. 

output
For each case you are to output a line giving the percentage of students whose grade is above average, rounded to 3 decimal places.'''

# n = int(input())
# for i in range(1, n+1):
#     student_num, *score = map(int, input().split())
#     sum = 0
#     count = 0
#     for j in range(student_num):
#         sum += score[j]
#     average = sum/student_num
    
#     for j in range(student_num):
#         if score[j] > average:
#             count +=1
#         result = (count/student_num)*100
#     print(str('%.3f' % result) +"%")

''' different code '''
# n = int(input())

# for _ in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1  # 평균 이상인 학생 수
#     rate = cnt/nums[0] *100
#     print(f'{rate:.3f}%')


''' [Question 15596] '''

# def sum_fun(a):
#     sum = 0
#     for i in a:
#         sum += i
#     return sum

''' [Question 4673] 
In 1949 the Indian mathematician D.R. Kaprekar discovered a class of numbers called self-numbers. For any positive integer n, define d(n) to be n plus the sum of the digits of n. (The d stands for digitadition, a term coined by Kaprekar.) For example, d(75) = 75 + 7 + 5 = 87. Given any positive integer n as a starting point, you can construct the infinite increasing sequence of integers n, d(n), d(d(n)), d(d(d(n))), .... For example, if you start with 33, the next number is 33 + 3 + 3 = 39, the next is 39 + 3 + 9 = 51, the next is 51 + 5 + 1 = 57, and so you generate the sequence
33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
The number n is called a generator of d(n). In the sequence above, 33 is a generator of 39, 39 is a generator of 51, 51 is a generator of 57, and so on. Some numbers have more than one generator: for example, 101 has two generators, 91 and 100. A number with no generators is a self-number. There are thirteen self-numbers less than 100: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, and 97.
Write a program to output all positive self-numbers less than 10000 in increasing order, one per line.'''

'''Code 1'''
# # 함수 d 구현하기
# def d(n):
#     n = n + sum(map(int, str(n)))
#     return n

# # 생성자가 있는지 확인할 리스트 초기화하기
# a = [0]*10001

# # 생성자 찾기
# for i in range(1, 10001):
#     a[i] = d(i)

# for i in range(1, 10001):
#     # 셀프넘버라면 출력하기
#     if i not in a:
#         print(i)



''' code 2 '''
# list1 = [i for i in range(1,10001)]
# self_num = []
# def func(n):
#     for i in range (1,n+1):
#         self_num_calc = i + sum(map(int, str(i)))
#         self_num.append(self_num_calc)
    
#     return self_num

# self_num = func(10000)
# for i in list1:
#     if i not in self_num:
#         print(i)


''' [Question 4673] '''
# c = input()
# print(ord(c))


''' [Question 11720] '''
''' First code '''
# import sys
# n = int(sys.stdin.readline())
# x = input()

# sum = 0
# for i in range(n):
#     sum += int(x[i])
# print(sum)

'''other code'''
# n = input()
# print(sum(map(int, input())))


''' [Question 10809] '''
''' Try 1, But Fail'''
# # 백준 인풋 받기
# c = input()
# # 결과 값 받을 리스트 만들기
# list1 = [-1]*26
# # 백준 알파벳을 list1 에 넣을 위치 정하기
# list2 = []
# for i in range(len(c)):
#     c_ord = ord(c[i]) - 97 # 97 는 a 의 아스키 코드
#     list2.append(c_ord)

# # index는 넣을 입력 값, j는 위치
# for index, j in enumerate(list2):
#     list1[j] = index

# for i in list1:
#     print(i, end=" ")

''' Another code '''

# # 문자열 입력
# s = list(map(str, input()))

# # 알파벳 리스트
# alpha = list('abcdefghijklmnopqrstuvwxyz')


# # 알파벳 길이만큼 array 에 -1
# array = [-1 for i in range(len(alpha))]

# for i in range(len(s)):
#     # 알파벳 리스트의 인덱스와 문자열 인덱스가 같으면 i
#     if array[alpha.index(s[i])] == -1:
#         array[alpha.index(s[i])] = i
# for j in array:
#     print(j, end=" ")



''' [Question 2675]
For this problem, you will write a program that takes a string of characters, S, and creates a new string of characters, T, with each character repeated R times. That is, R copies of the first character of S, followed by R copies of the second character of S, and so on. Valid characters for S are the QR Code "alphanumeric" characters:
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%*+-./:

input
The first line of input contains a single integer P, ( 1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set is a single line of input consisting of the data set number N, followed by a space, followed by the repeat count R, ( 1 ≤ R ≤ 8), followed by a space, followed by the string S. The length of string S will always be at least one and no more than 20 characters. All the characters will be from the set of characters shown above.

output
For each data set there is one line of output. It contains the data set number, N, followed by a single space which is then followed by the new string T, which is made of each character in S repeated R times.'''
n = int(input())

for _ in range(n):
    a, b = map(str, input().split(" "))
    a = int(a)

    for i in b:
        print(i*a, end="")
    print()















