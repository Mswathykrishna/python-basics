#CHECK FOR PALINDROME
def is_palinbdrome(s):
    return s==s[::-1]
string=input("Enter a string:")
if is_palindrome(string):
    print("palindrome")
 else:
    print("Not a palindrome")
