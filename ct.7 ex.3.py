from random import randint

def Read_Score():
    Scores = ()
    Done = True
    count = 1
    while Done:
        score = int (input(f"Enter score #{count} (-1 to exit): "))
        if score >= 0 and score <= 100:
            Scores += (score,)
            count += 1
        elif score == -1:
            break
        count -= 1
        return (Scores)
def Check_Grade(Scores):
    Grades = ()
    for score in Scores:
        grade = ""
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        Grades += (grade,)
        return(Grades)
def Roport_Grade(Scores,Grades):
    Max = len(Scores)
    print("="*24)
    print("| No. | Scores | Grade |")
    print("="*24)
    for n in range(Max):
        print(f"| %2d  |  %3d   |   %s   |"%(n+1,Scores[n],Grades[n]))
    print("="*24)

Scores = Read_Score()
Grades = Check_Grade(Scores)
Roport_Grade(Scores,Grades)

print(f"End Program")
