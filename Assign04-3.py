E = True
cof = tol = q = 0
n = 1
val = []
val2 = []
val3 = []
val4 = []
while E:
    print(f"""======================= 
| Drinks Menu         | 
======================= 
| 0. Quit             | 
| 1. Hot Coffee       | 
| 2. Ice Coffee       | 
| 3. Frappe Coffee    | 
| 4. Calculate Cost   | 
=======================
""")
    orde = int(input("Select Item :"))
    if orde == 0:
        E = False
    if orde == 1:
        cof = int(input("Hot Coffee, how many glasses :"))
        name = "Hot Coffee"
        prc = 35.00
        To =cof*prc
        q=q+1
        val.append(cof)
        val2.append(name)
        val3.append(prc)
        val4.append(To)
    elif orde == 2:
        cof = int(input("Ice Coffee, how many glasses :"))
        name = "Ice Coffee"
        prc = 50.00
        To =cof*prc
        q=q+1
        val.append(cof)
        val2.append(name)
        val3.append(prc)
        val4.append(To)
    elif orde == 3:
        cof = int(input("Frappe Coffee, how many glasses :"))
        name = "Frappe Coffee"
        prc = 60.00
        To =cof*prc
        q=q+1
        val.append(cof)
        val2.append(name)
        val3.append(prc)
        val4.append(To)
    elif orde == 4:
        print(f"""Order #{n}: 
----------------------------------- 
Qty Item Price Total 
-----------------------------------""")
        n+=1 
        for i in range(0,q):  
            print(f"{val[i]} {val2[i]} {val3[i]} {val4[i]}")
            tol = val4[i] + tol
        print(f"""-----------------------------------
Total: {tol} Bath""")
        val.clear()
        val2.clear()
        val3.clear()
        val4.clear()
        q=0
        tol=0
    else:
        print("Some thing went wrong.")
