def is_palindrome(s):
    return s==s[::-1]
print(is_palindrome("madam"))


def are_anagrams(s1,s2):
    return sorted(s1)==sorted(s2)
print(are_anagrams("silent","listen"))
