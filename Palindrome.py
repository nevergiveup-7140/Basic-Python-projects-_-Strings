def palindrome(words):
    
        if words == words[::-1]:
            print("it is a palindrome")
        else:
            print("It's not in palindrome")
        return
palindrome(input("Type your word : "))