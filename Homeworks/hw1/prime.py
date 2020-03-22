def prime(num):
    if num <= 1:
        return False
    
    for i in range(2,num):
        if( num % i == 0):
            return False
    
    return True


x = int(input("Please input the number to be checked:\t"))

print(str(x), "is a prime" if prime(x) else "is not a prime")