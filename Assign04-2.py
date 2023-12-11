print("""=========================================
| Program Calculate Grade Point Average |
=========================================
Input Data:""")
       
val = []
val2 = []
val3 = []
val4 = []
tol = 0
for n in range(1, 6):
    na = input(f"Enter subject name ({n}): ")
    val.append(na)
    na2 = float(input(f"Enter subject score ({n}): "))
    print ()
    
    if na2 > 79:
        gra = "A"
        poi = 12.0
    elif na2 > 69:
        gra = "B"
        poi = 9.0
    elif na2 > 59:
        gra = "C"
        poi = 6.0
    elif na2 > 49:
        gra = "D"
        poi = 3.0
    elif na2 < 50:
        gra = "F"
        poi = 0.0
    else:
        print("Something in the score went wrong")

    val2.append(na2)
    val3.append(gra)
    val4.append(poi)

print("""Grade Point Average(GPA) Report
=========================================
No. Subject Name Mark Grade Points
=========================================""")

for i in range(5):
    print(f"{i + 1}. {val[i]}    {val2[i]}    {val3[i]}    {val4[i]}")
    tol = val4[i] + tol
print(f"""=========================================
Total Points : {tol}
Total Credits : 15.0
Grade Point Average(GPA) : {tol/15}""")
