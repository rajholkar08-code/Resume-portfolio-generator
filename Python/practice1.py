#Count character
text = input()
ch = input()
count = 0
for i in text:
    if i == ch:
        count += 1
print(count)

#Palindrome check
text = input()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Word counter
sentences = input()
word = sentences.split()
print(len(word))

#Remove space from string
text = input()
space = text.replace(" ","")
print(space)

#Capatalize first letter
text = input()
print(text.title())

#Longest word finder
a=input().split()
l=a[0]
for i in a:
    if len(i)>len(l):
        l=i
print(l)

#Remove duplicates characters
a=input()
b=""
for i in a:
    if i not in b:
        b+=i
print(b)

#anagram checker
s1=input()
s2=input()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#Character with maximum frequency
s = input()
max_char = max(s, key=s.count)
print(max_char)

#String comprehension
s = input("Enter a string: ")
compressed = ""

for ch in set(s):
    compressed += ch + str(s.count(ch))

print(compressed)