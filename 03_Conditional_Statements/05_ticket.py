a1 = 100
a2 = 150
a3 = 300
t100 = int(input("Enter number of Rs.100 tickets: "))
t150 = int(input("Enter number of Rs.150 tickets: "))
t300 = int(input("Enter number of Rs.300 tickets: "))
paid = int(input("Enter amount paid: "))
total = (t100 * a1) + (t150 * a2) + (t300 * a3)
print("Total Ticket Price =", total)
if paid >= total:
    print("Return Amount =", paid - total)
else:
    print("less Amount! Need", total - paid, "more.")