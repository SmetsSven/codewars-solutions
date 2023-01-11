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
