# Detect if given integer is palindrome

def is_palindrome(n):
    str_n = str(n)
    reverse_str_n = str_n[::-1]
    if str_n == reverse_str_n:
        return True
    else:
        return False
    

print(is_palindrome(12345))
print(is_palindrome(123454321))
print(is_palindrome(11011))
