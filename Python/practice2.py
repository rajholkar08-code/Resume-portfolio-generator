'''def prime_or_not(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

l=[2,3,4,5,6,7,11,8,13]
res=[]
for n in l:
    if prime_or_not(n):
        res.append(n)
print(res)

def sides(l,b):
    a=l*b
    p=2*(l+b)

    print(a)
    print(p)
l=int(input())
b=int(input())
sides(l,b)

def rad(r):
    a=3.14*r*r
    c=2*3.14*r
    print(a)
    print(c)
r=int(input())
rad(r)

def numbers(a,b):
    c=a**b
    print(c)
a=int(input())
b=int(input())
numbers(a,b)

def vote(a):
    if (a>18):
        print("yes")
    else:
        print("no")
a=int(input())
vote(a)

def num(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
n=int(input())
num(n)

def prime_or_not(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if prime_or_not(n):
    print("prime")
else:
    print("not prime")

a=int(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

fact_dict={}

def factorial(n):
    if n==0 or n==1:
        return 1
    
    if n in fact_dict:
        return fact_dict[n]
    fact_dict[n] = n * factorial(n-1)
    return fact_dict[n]
n=int(input())
print(factorial(n))
print(fact_dict)

def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact*i
    return fact
n=int(input())
print(factorial(n)

def prime_or_not(n):
    for i in range(2,n):
        if n%i==0:
            return "Not Prime"
    return "Prime"
n=int(input())
print(prime_or_not(n))

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
n=int(input())
print(fib(n))

def greet(name="Student"):
    print("Hello", name)

greet()

#String
s=input()

for ch in s:
    if s.count(ch)==1:
        print(ch)
        break

s=input().split()
longest=max(s,key=len)
print(longest)

s=input()
res=""
for ch in s:
    if ch not in res:
        res+=ch
print(res)

s=input()
res=""
for ch in s:
    res+=ch

if s==res:
    print("Pallindrome")
else:
    print("Not palindrome")

s=input()
print(max(s,key=s.count))

s = input().split()

print(" ".join(s[::-1]))

s=input()
v=0
c=0

res="aeiouAEIOU"
for ch in s:
    if s.isalpha():
        if ch in res:
            v+=1
        else:
            c+=1

print(v)
print(c)

lst=list(map(int,input().split()))
res=[]
for ch in lst:
    if ch not in res:
        res.append(ch)
print(res)

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(list(set(a) & set(b)))

d = {"a":1, "b":2}
new={v:k for k,v in d.items()}
print(new)

import numpy as np

a=np.array(list(map(int,input().split()))).reshape(2,2)

print("Matrix : ",a)

print(a.sum(axis=1))

print(a.sum(axis=0))'''

lst = [[1,2],[3,4],[5]]

flat = []

for i in lst:
    flat.extend(i)

print(flat)