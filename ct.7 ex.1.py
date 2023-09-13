def Check_Grade(grade):
    Grade = ('A','B','C','D','F')
    Value = (4,3,2,1,0)
    for n in range(len(Grade)):
        if grade == Grade[n]:
            return(Value[n])

Done = True
while Done:
    grade = input("Enter grade (Q-exit): ")
    print()
    grade = grade.upper()
    if grade == "Q":
        break
    else:
        value = Check_Grade( grade)
        print (f"Score value of {grade} is {value}")
        print()

print("End Program.")
