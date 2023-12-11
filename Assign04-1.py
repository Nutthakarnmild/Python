ME = True
while ME :
    num = int(input("Enter number(2-12) :"))
    print("""---------------------------------------------------------
                    Multiplication Table
---------------------------------------------------------""")
    for i in range (1,13):
        print(f"| {num} X {i:2} = {num * i:2} | {num + 1} X {i:2} = {(num + 1) * i:2} | {num + 2} X {i:2} = {(num + 2) * i:2} | {num + 3} X {i:2} = {(num + 3) * i:2} |")
        if num == 0:
            C = False
