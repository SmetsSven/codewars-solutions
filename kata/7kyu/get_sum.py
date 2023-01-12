# https://www.codewars.com/kata/55f2b110f61eb01779000053/python

def get_sum(a: int,b: int)-> int:
    """Get sum of all integers inbetween
    
    Args:
        a: integer, that can be start or end value
        b: integer, that can be start or end value
        
    Return: 
        Sum of integers between the two given numbers
    """
    result = 0
    
    for i in range(min(a,b), (max(a,b)+ 1)):
        result += i
        
    return result
    
