menuStr = 'Main Menu \n----------\n 1. Exercise 1\n 2. Exer 2\n'
menuStr += '3. 3\n4. Exit \nSelect chioce'
MainLoop = True
while MianLoop:
    choice == '1'
        print(">> Program Find Maximum DIgit <<")
        done = True

        while done:
            numStr = input('Enter integer number (0-exit) : ')
            if numStr == '0':
                done  = False
            else:
                Max = 0
                #for n in range (len(numStr)):
                #    digitStr = numStr[n]
                #for digitStr in numStr:
                #    digitStr = int(digitStr)
                #    if digit > Max:
                #        Max = digit
                num = int (numStr)
                while num > 0:
                    digit = num % 10
                    num = num // 10
                    if digit > Max:
                        Max = digit
                print(f"Maximum digit of intger {numStr} = {Max}")

        print("Exit Program")
    elif chioce == '2':
        pass
    elif chioce == '3':
        pass
    elif chioce == '4':
        pass
        MianLoop = False
