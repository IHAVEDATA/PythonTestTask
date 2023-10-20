
userString = input("Enter string here: ")

def isPalindrome(word):
    word = word.replace(" ", "").lower()
    
    return word == word[::-1]

print(isPalindrome(userString))