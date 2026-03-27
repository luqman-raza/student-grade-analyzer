
name = input("What is your name? ")
marks = int(input("Write student marks? "))


if marks > 100 or marks < 0:
    print("You gave out-of-range marks. Please enter 0-100.")
else:
    if marks >= 90:
        grade = "A"
        status = "Excellent! Keep it up 🎉"
    elif 75 <= marks <= 89:
        grade = "B"
        status = "Good job! You can improve more 💪"
    elif 50 <= marks <= 74:
        grade = "C"
        status = "Fair. Study harder 📚"
    else:
        grade = "Fail"
        status = "You need to work hard 😅"

    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")