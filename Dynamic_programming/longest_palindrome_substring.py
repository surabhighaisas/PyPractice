# Find longest palindrome substring in a given string

# Solution 1: Expand around center to find longest palindrome.
# Time complexity O(n^2), space complexity O(1)
def longestPalindrome(s: str) -> str:
        current_max = 0
        L_max = 0
        R_max = 0
        str_len = len(s)

        def max_palindrome_length(l, r):
            while l >= 0 and r < str_len and s[l] == s[r]:
                l-= 1
                r+= 1
            return (r - l - 1), l+1, r-1
            
        for i in range(str_len):
            odd, ol, o = max_palindrome_length(i,i)
            even, el, er = max_palindrome_length(i,i+1)
            if odd > even:
                if odd > current_max:
                    current_max = odd
                    L_max = ol
                    R_max = o
            else:
                if even > current_max:      
                    current_max = even
                    L_max = el
                    R_max = er

        return s[L_max: R_max+1]


print(longestPalindrome("pqrababaxy"))
print(longestPalindrome("aabbccbbaa"))

# solution 2: Using dynamic programming
# Time complexity O(n^2), space complexity O(n ^ 2)

def longestPalindrome_dp(s: str) -> str:
    str_len = len(s)
    if str_len <= 1:
        return s
    
    max_len = 1
    max_str = s[0]
    
    store = [[False for _ in range(str_len)] for _ in range(str_len)]

    for i in range(str_len):
        store[i][i] = True
        for j in range(i):
            if s[j] == s[i] and (i - j <= 2 or store[j+1][i-1]):
                store[j][i] = True
                if i -j + 1 > max_len:
                    max_len = i-j+1
                    max_str = s[j:i+1]
                    #print(max_str)
    return max_str


print(longestPalindrome_dp("pqrababaxy"))
print(longestPalindrome_dp("aabbccbbaa"))
