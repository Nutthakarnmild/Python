Total = 0.0
Score = ""
Count = 1
while Score != "-1":
    Score = input(f"Enter score value #{Count} : ")
    if Score  != "-1":
        Count += 1
        Total += float(Score)

Count -= 1
print ("Number of Score : ", Count)
print ("Total Score value : ",Total)
print ("Average Score : %.2f"% (Total/Count))
