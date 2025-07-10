# Find longest palindrome substring in a given string

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
