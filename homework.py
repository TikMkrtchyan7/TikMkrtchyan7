##Վարժություն 1.11
#Recursion

def positive(n):
    if n<0:
        return "Does not much"
    if n<3:
        return n
    else :
        if n>3:
            return n
        return positive(n-1) + positive(n-2) + positive(n-3)

#Tail recursion

def positive(n, a=0, b=1, c=2):
    return a if n == 0 else positive(n - 1, b, c, a + b + c)


##Վարժություն 1.12

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def pas(n,m):
    if (m < 0 or n<m):
        return "Wrong Input!"
    return fact(n)/(fact(m)*fact(n-m))
