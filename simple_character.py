char = input("Enter a single charecter:")
if len(char) == 1 and char.isalpha():
    vowels = 'aeiou'
    if char in vowels:
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consunant.")
else:
    print("invalid input. please input a single alphabetic charecter")
