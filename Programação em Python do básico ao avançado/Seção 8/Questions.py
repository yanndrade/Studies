from math import sqrt
import time

#Help Functions

def get_key_from_value(d,value):
    return [k for k,v in d.items() if v == value][0]

def get_list_of_divisors(num):
    lst_divisors = [n for n in range(1,num+1) if num%n == 0]
    return lst_divisors

def isPrime(num):
    if(len(get_list_of_divisors(num)) == 2): 
        return True
    else:
        return False
    
def GCD(a,b):
    diva = set(get_list_of_divisors(a))
    divb = set(get_list_of_divisors(b))

    div = diva & divb
    return max(list(div))



# Questions

def q1(num):
    return 2*num

def q2(date):
    months = dict(january=1,february=2,march=3,april=4,may=5,june=6,july=7,august=8,september=9,october=10,november=11,december=12)


    day = int(date[0:2])
    month = get_key_from_value(months,int(date[3:5]))
    year = int(date[6:])

    print(f"Today is {day} of {month} of {year}")


def q3(num):
    if num<0:
        return -1
    elif num>0:
        return 1
    else:
        return 0


def q4(num):

    if (num<0) or (type(num) !=  int):
        return False
    divisors = get_list_of_divisors(num)

    for n in divisors:
        if num == n**2:
            return True
        
    return False


def q5(radius):
    return 4*3.1415*(radius**3)/3


def q6(hour,minutes,seconds):
    return hour*3600 + minutes*60 + seconds


def q7(celsius):
    return (celsius*9/5) + 32

def q8(a,b):
    return(sqrt(a**2 + b**2))

def q9(r,h):
    pi = 3.141592
    return pi*(r**2)*h

def q10(a,b):
    if a<b:
        return b
    else:
        return a

def q11(tpe, *args):
    a,b,c = args

    if len(args) == 3:
        if tpe == 'A' or tpe == 'a':
            return sum(args)/len(args)  
        elif tpe == 'P' or tpe == 'p':
            a = 5*a + 3*b + 2*c
            return a/10
        else:
            print("Error")
            return -1
    else:
        print("Error")
        return -1
    
def q12(num):
    if num<0:
        print("Error")
        return-1
    else:
        temp = [int(i) for i in str(num)]
        return sum(temp)

def q13(num1,num2,ope):
    match ope:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            return num1/num2
        case '*':
            return num1*num2
        

def q14(dist,gaso):
    km_l = dist/gaso

    if km_l < 8:
        print("Venda o Carro!")
    elif km_l > 12:
        print("Super economico!")
    else:
        print("Economico!")


def q15(*args):
    if len(args) == 3:
        a,b,c = args
        l = {a,b,c}
        if (a!=0) & (b!=0) & (c!=0) & (a<b+c) & (b<a+c) & (c<b+a):
            if len(l) == 1:
                print("Equilateral triangle")
            elif len(l) == 2:
                print("Isosceles triangle")
            else:
                print("Scalene triangle")
        else:
            print("Its not a Triangle")

    else:
        print("3 values necessary!")
        

def q16(num):
    print(num*'=')

def q17(a,b):
    if (a>0) & (b>0):
        values = list(range(a+1,b))
    else:
        print("Erro: Only positive integers")
        return -1
    return sum(values)


def q18(X,Z):

    if(Z == 1):
        return X*1
    else:
        return X*q18(X,Z-1)


def q19(num):
    div = get_list_of_divisors(num)
    for divisors in div[::-1]:
        if(isPrime(divisors)):
            return divisors


def q20(n):

    if(n == 0):
        return 1
    else:
        return n*q20(n-1)

def q21(N):
    lst = [n for n in range(N) if isPrime(n)]
    print(lst)


def q22(n):
    for i in range(1,n+1):
        print(i*'!')

def q23(n):
    for i in range(1,2*n):
        if i > n:
            print((2*n-i)*'*')
        else:
            print(i*'*')

def q24(n):
    for i in range(1,2*n-1):
        print((2*n-i+1)*' ' + (2*i-1)*'*'+ (2*n-i+1)*' ')


def q25(N):
    S = 0
    for i in range(1,N+1):
        fact = (i**2 + 1)/(i + 3)
        S += fact
    return S

def q26_1(n):
    start = time.time()
    return sum(range(1,n+1)), start, time.time()

def q26_2(n):
    start = time.time()
    S = 0
    for i in range(1,n+1):
        S += i
    return S, start, time.time()


def q27(x,n):
    x = x*3.141593/180
    S = 0
    for i in range(n+1):
        fact = ( ((-1)**i) * ( x**(2*i+1) ) )/( q20(2*i +1) )
        S += fact
    return S
 #q20   

def q28(x,n):
    x = x*3.141593/180
    S = 0
    for i in range(n+1):
        fact = ( ((-1)**i) * ( x**(2*i) ) )/( q20(2*i) )
        S += fact
    return S

def q29(x,n):
    x = x*3.141593/180
    S = 0
    for i in range(n+1):
        fact = (( x**(2*i+1) ) )/( q20(2*i +1) )
        S += fact
    return S

def q30(x,n):
    x = x*3.141593/180
    S = 0
    for i in range(n+1):
        fact = (( x**(2*i) ) )/( q20(2*i) )
        S += fact
    return S

def q31(n):
    return sum([(1/q20(i)) for i in range(n)])

def q32(a,b):
    fact = GCD(a,b)
    print(f"{a}/{b} -> {int(a/fact)}/{int(b/fact)}")

def q33(n):
    fact = q20(n)
    s = 0
    for alg in str(fact):
        s += int(alg)
    return s
    
def q34(n):
    prod = 1
    for i in range(1,n+1):
        if(i%2 != 0):
            prod *= i
    return prod

def q35(n):
    return q20(2*n)/q20(n) 

def q36(n):
    prod = 1
    for i in range(1,n+1):
        prod *= q20(i)
    return prod

def q37(n):
    prod = 1
    for i in range(1,n+1):
        prod *= q18(i,i)
    return prod

def q38(n):
    return n**(q20(n-1))

# Test

print(q37(3))

