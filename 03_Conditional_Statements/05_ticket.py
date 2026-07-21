a=30
b=30
c=20
print(f"seats available at cost rs 100 are{a}")
print(f"seats available at cost rs 150 are{b}")
print(f"seats available at cost rs 300 are{c}")
d=int(input("Enter how many 100 rs tickets need to book "))
e=int(input("Enter how many 150 rs tickets need to book "))
f=int(input("Enter how many 300 rs tickets need to book "))
a-=d
b-=e
c-=f
g=(d*100)+(e*150)+(f*300)
print(f"total cost of your tickets is {g}")
h=int(input("enter the value total price shown above "))
if h==g:
    print("Thank you for giving exact amount")
    print(f"your tickets rs 100-{d} and rs 150-{e} and rs 300-{f} is booked")
elif h>g :
    print(f"take your change {h-g}")
    print(f"your tickets rs 100-{d} and rs 150-{e} and rs 300-{f} is booked")
else :
    print(f"enter {g} or above it")