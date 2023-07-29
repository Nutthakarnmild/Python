credit = int (input("Enter number money withdraw : "))

TS = credit/1000
FH = (credit%1000)/500
HD = (credit%500)/100

print (("Cash B1000 : "),int(TS))
print (("Cash B500 : "),int(FH))
print (("Cash B100 : "),int(HD))
