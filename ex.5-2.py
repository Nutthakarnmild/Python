total = 0.0
Max = 6
for n in range (1,Max):
    score = float(input(f"Enter Score #{n} :"))
    total = total + score
print()
print("Total score xalur : ",total)
print("Averange score : ",total/5)
