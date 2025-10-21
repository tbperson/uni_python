while True:
    try:
        score = int(input("Enter your score (0-100): "))
        if 100 >= score >= 70:
            print("First Class")
            break
        elif 69 >= score >= 60:
            print("2:1")
            break
        elif 59 >= score >= 50:
            print("2:2")
            break
        elif 49 >= score >= 40:
            print("Third Class")
            break
        elif 39 >= score >= 0:
            print("Fail")
            break
        else:
            print("Score out of range. Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")