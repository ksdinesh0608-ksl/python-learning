print("Available Branches : cse, ece, ce, me, eee")
a= input("Enter the first two letters of the branch: ").upper()
if len(a) != 2:
    print("Invalid input! Please enter exactly two letters.")
elif a == "CS" or a == "CSE":
    print("You selected (CSE)")
elif a == "EC" or a == "ECE":
    print("You selected (ECE)")
elif a == "CE" :
    print("You selected (CE)")
elif a == "ME":
    print("You selected (ME)")
elif a == "EE" or a == "EEE":
    print("You selected (EEE)")
else:
    print("Invalid branch code")