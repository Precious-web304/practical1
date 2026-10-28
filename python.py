# input score by teacher
if __name__ == "__main__":
    score = float(input("Enter the score (0-100): "))
    if score >= 70:
        grade = 'A'
    elif score >= 69:
        grade = 'B'
    elif score >= 59:
        grade = 'C'
    elif score >= 49:
        grade = 'D'
    elif score >= 39:
        grade = 'F'
    
    print(f"The grade for the score {score} is: {grade}")
    # input score by teacher
    # students name and score
    name = input("Enter the student's name: ")
    print(f"Student: {name}, Score: {score}, Grade: {grade}")
    print("graded by teacher")

