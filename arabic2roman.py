# Erin Thomas / U26838058 / EC 500: Building Software / Assignment 1
# Program to convert Arabic numbers to Roman numerals
# Reference: https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/

def arabic2roman(number):
    # Error check
    if number == 0:
        print("Integer must be greater than zero.")
        return ''
        
    if number < 0:
        print("Integer must be greater than zero.")
        return ''
    
    if number > 3999:
        print("Integer must be less than 4000.")
        return ''

    if type(number) != int:
        print("Must be an integer.")
        return ''
    
    arabic_num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_symb = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = 12
    roman_final = ''

    # Repeats until remainder is zero
    while number:
        # Repeats until quotient is zero
        quot = number // arabic_num[i]
        number %= arabic_num[i]

        # Prints roman numerals equivalent to quotient (e.g. 2300/1000 --> quot = 2, so M will print twice )
        while quot: 
            #print(roman_symb[i])
            roman_final += roman_symb[i] # Fixes spacing issue
            quot -= 1
        i -= 1
    return roman_final


