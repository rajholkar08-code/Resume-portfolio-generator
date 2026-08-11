# a=int(input())
# b=int(input())
# print(a+b)

# side = int(input("Enter side : "))
# area = side * side
# print(area)

# a = float(input("Enter first number : "))
# b = float(input("Enter second number : "))
# print("average = ", (a+b)/2)

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# if(a>=b):
#     print("True")
# else:
#     print("False")
# or
# print(a>=b)

# name = input("Enter your name : ")
# print(len(name))

# str = "swifhuiwhgfuowehgouiqahegobh"
# print(str.count("w"))

# num = int(input("Enter number : " ))
# if(num%2==0):
#     print("even")
# else:
#     print("odd")

# num = int(input("Enter number : "))
# if(num%7==0):
#     print("multiple of 7")
# else:
#     print("not multiple of 7")

str1 , str2 = input().split()
if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)

# sentences = input().lower()

# letters = "abcdefghijklmnopqrstuvwxyz"
# flag = True

# for ch in letters:
#     if ch not in sentences:
#         flag = False
#         break
# print(flag) 


# s = input("Enter string: ")
# print(s[::-1])

# def add(a,b):
#     return(a+b)
# print(add(5,998))

# start = int(input("Enter start number : "))
# end = int(input("Enter end number : "))
# count = 0
# for i in range(start, end+1):
#     if i % 2 != 0:
#         count += 1
# print("Odd numbers count:", count)

# num = int(input("Enter a number : "))
# if '7' in str(num):
#     print("Lucky digit bonus")
# else:
#     print("No Bonus")

# value = input()
# if value.isdigit():
#     print("int")
# else:
#     try:
#         if "." in value:
#             print("float")
#         else:
#             print("int")
#     except:
#         print("str")

# num = int(input("Enter a number : "))
# for i in range(1,11):
#     print(num ** num)

# start = int(input("Enter start number : "))
# end = int(input("Enter end number : "))
# count = 0
# for i in range(start, end + 1):
#     if i%2!=0:
#         count += 1
# print(count)

# num = int(input("Enter a number : "))
# if '7' in str(num):
#     print("lucky")
# else:
#     print("NO lucky")

# s = input("Enter a string: ")

# if s[0].isupper():
#     print(s, "- First letter is Capital")
# else:
#     print(s, "- First letter is Not Capital")

# x = set(map(int,input().split()))
# y = set(map(int,input().split()))
# common = x.intersection(y)
# print(common)

