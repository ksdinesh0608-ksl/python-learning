print("Select Your Qualification")
print("1. Intermediate")
print("2. Diploma (Lateral Entry)")
admission = int(input("Enter your choice: "))

if admission == 1:

    print("Available Courses")
    print("1. B.Tech CSE")
    print("2. B.Tech AIML")
    print("3. B.Tech ECE")
    print("4. B.Tech EEE")
    print("5. B.Tech Civil")
    print("6. B.Tech Mechanical")

    course = int(input("Select your course: "))

    if course == 1:
        course_name = "B.Tech CSE"
    elif course == 2:
        course_name = "B.Tech AIML"
    elif course == 3:
        course_name = "B.Tech ECE"
    elif course == 4:
        course_name = "B.Tech EEE"
    elif course == 5:
        course_name = "B.Tech Civil"
    elif course == 6:
        course_name = "B.Tech Mechanical"
    else:
        print("Invalid Course")
        course_name = "None"

    fee = 200000
    duration = 4

elif admission == 2:

    print("Eligible Courses")
    print("1. B.Tech CSE")
    print("2. B.Tech AIML")
    print("3. B.Tech ECE")
    print("4. B.Tech EEE")
    print("5. B.Tech Civil")
    print("6. B.Tech Mechanical")

    course = int(input("Select your course: "))

    if course == 1:
        course_name = "B.Tech CSE"
    elif course == 2:
        course_name = "B.Tech AIML"
    elif course == 3:
        course_name = "B.Tech ECE"
    elif course == 4:
        course_name = "B.Tech EEE"
    elif course == 5:
        course_name = "B.Tech Civil"
    elif course == 6:
        course_name = "B.Tech Mechanical"
    else:
        print("Invalid Course")
        course_name = "None"

    fee = 150000
    duration = 3

else:
    print("Invalid Choice")
    fee = 0

if fee > 0:

    total_fee = fee * duration
    reservation_fee =fee * 0.25
    print("Course               :", course_name)
    print("Duration             :", duration, "Years")
    print("Fee Per Year         : ₹", fee)
    print("Total Fee            : ₹", total_fee)
    print("Reservation Fee(25%) : ₹", reservation_fee)

    pay = float(input("Enter Reservation Fee: ₹"))

    if pay == reservation_fee:
        print("Congratulations!")
        print("Your seat has been reserved successfully.")
    else:
        print("Reservation amount is incorrect.")
        print("Your seat has not been reserved.")