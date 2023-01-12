# https://www.codewars.com/kata/54b724efac3d5402db00065e

import re
from preloaded import MORSE_CODE

def decode_morse(morse_code: str) -> str: 
    """Decode given morse code
    
    Args:
      morse_code: Morse code that needs to be decoded

    Returns:
      The decoded morse code.  
    """

    words = re.split("(\   )", morse_code.strip())  # splits the morse code in words, and removes the trailing spaces
    decoded_word = ""
    
    for word in words:
        word = word.split(" ") if word != "   " else [''] # if three spaces are found, the word is replaced by blank space 
        for letter in word:
            decoded_word += MORSE_CODE.get(letter, ' ')
    
    return decoded_word
