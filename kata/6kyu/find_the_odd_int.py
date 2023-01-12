# https://www.codewars.com/kata/54da5a58ea159efa38000836

import pandas as pd

def find_it(seq: list)-> int:
    """Find value that appears an odd number of times in the list
    
    Args:
        seq: list with integer value, one reappearing an odd number of times
      
    Returns:
        The number that appears an odd number of times
        
    Raise: 
        ValueError: If no number appears an odd number of times
    """
    
    result = pd.Series(seq).value_counts()
    
    for key, value in result.items():
        if value % 2 != 0:
            return key
    
    raise ValueError("The given list must contain one number that appears an odd number of times.")
