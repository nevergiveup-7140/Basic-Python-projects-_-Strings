def your_data(password):
    has_upper=False
    has_specials=False
    has_digits=False
    
    specials = ('.','!','@','#','$','%','&','*','?')
    
    for i in password:
        if i.isupper():
            has_upper=True
        if i in specials:
            has_specials=True
        if i.isdigit():
            has_digits=True
    
    if has_digits and has_specials and has_upper:
        print("unbreakable")
    elif  has_specials and has_upper:
        print("Good")
    elif has_specials :
        print("Ok")
    else:
        print("Weak Password")
your_data(input("Enter your password: "))