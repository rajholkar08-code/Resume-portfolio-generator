def prime_or_not(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    else:
        return True
    
if prime_or_not():
    print("prime")
else:
    print("not prime")