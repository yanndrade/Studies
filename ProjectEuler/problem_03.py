def get_list_of_divisors(num):
    lst_divisors = [n for n in range(1,num+1) if num%n == 0]
    return lst_divisors

def isPrime(num):
    print(num)
    if(len(get_list_of_divisors(num)) == 2): 
        return True
    else:
        return False
    
def get_highest_prime_divisor(num):
    div = get_list_of_divisors(num)
    for divisors in div[::-1]:
        if(isPrime(divisors)):
            return divisors
        
        
print(get_highest_prime_divisor(600851475143))

