# https://www.codewars.com/kata/525f4206b73515bffb000b21
# Create a function named divisors/Divisors that takes an integer n > 1
# and returns an array with all of the integer's divisors(except for 1 and the number itself),
# from smallest to largest. If the number is prime return the string '(integer) is prime'

def divisors(integer):
    """Get array of divisors or check if prime number
    
    Keyword arguments: 
    integer -- positive integer bigger then 1
    """
    if integer < 1: 
        raise("integer needs to be bigger then 1")
        
    result = [(i) for i in range(2, integer) if integer % i == 0] 

    if len(result) == 0:
        return f"{integer} is prime"
    
    return result
