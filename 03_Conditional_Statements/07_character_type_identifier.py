ch= input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter only one character.")
elif ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Number")
else:
    print("Special Character")