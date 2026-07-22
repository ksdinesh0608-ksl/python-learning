a=(input("enter a value")).lower()
count=0
for n in a:
    if n in "aeiou":
        count=count+1
print("count of vowels is",count)