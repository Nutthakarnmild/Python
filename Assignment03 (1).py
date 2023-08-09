num = int(input ("ใส่ค่าเลขฐานสิบ (1-15) : "))

num1 = num
num2 = (num // 2)
num3 = (num2 // 2)
num4 = (num3 // 2)

print ("เป็นเลขเลขฐานสอง",(num4 % 2),(num3 % 2),(num2 % 2),(num1 % 2))
