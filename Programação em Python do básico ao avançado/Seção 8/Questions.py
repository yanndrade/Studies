from math import sqrt

#Help Functions

def get_key_from_value(d,value):
    return [k for k,v in d.items() if v == value][0]

def get_list_of_divisors(num):
    lst_divisors = [n for n in range(1,num) if num%n == 0]
    return lst_divisors


# Functions

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

    if tpe == 'A' or 'a':
        return sum(args)/len(args)
    if tpe == 

# Test
print(q9(1,1))