# (1.)
# data = input().split()
# text = data[0].strip('"')
# sub = data[1].strip('"')

# count = 0
# for i in range(len(text) - len(sub) + 1):
#     if text[i : i + len(sub)] == sub:
#         count += 1

# print(count)

# (2.)
# data = input().split()

# if len(data) == 2:
#     str1 = sorted(data[0].strip('"'))
#     str2 = sorted(data[1].strip('"'))
    
#     print(str1 == str2)
# else:
#     print(False)

# (3.)
# s = input()
# sentence = s.strip('"').lower()

# letters = set()

# for ch in sentence:
#     if 'a' <= ch <= 'z':
#         letters.add(ch)

# print(len(letters) == 26)

# if i < len(S1):
#     out = out + S1[i]
#     i += 1
# if j < len (S2):
#     out += S2[j]
#     j += 1
# print(out)

l=[]
for i in range(1,101):
    if i%10==0:
        l.append(i)
print(i)