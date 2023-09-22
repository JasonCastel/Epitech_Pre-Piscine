def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

print(is_palindrome("kayak"))  
print(is_palindrome("never odd or even"))  
print(is_palindrome("Was it a car or a cat I saw?"))  
print(is_palindrome("hello")) 
