# Detect if given integer is palindrome

# With string conversion
def is_palindrome(n):
    str_n = str(n)
    reverse_str_n = str_n[::-1]
    if str_n == reverse_str_n:
        return True
    else:
        return False

# Without string conversion    
def is_palindrome_without_string_conversion(n):
    temp = n
    reverse = 0
    while(temp != 0):
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    if reverse == n:
        return True
    else:
        return False

print(is_palindrome(12345))
print(is_palindrome(123454321))
print(is_palindrome_without_string_conversion(11011))
