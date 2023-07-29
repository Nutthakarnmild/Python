a = int (input("Enter amount : "))
r = float (input("Enter rate : "))/100
y = int (input("Enter year : "))

FV = (a*(1+r)**y) 

print (("Future value = "),float(FV))
