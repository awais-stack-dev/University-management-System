import random
list = []
i = 0
correct=0
wrong=0
while i < 10:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    opt = random.randint(1,5)
    if opt == 1:
        ans = int(input(str(num1)+" + "+str(num2)+"= "))
        if ans == num1 + num2:
            list.append((str(num1) + "+" + str(num2) + "= " + str(ans) + " (Correct) "))
            correct+=1
        else:
            list.append(
                (str(num1) + "+" + str(num2) + "= " + str(ans) + " (Incorrect) Correct answer is " + str(num1 + num2)))
        i += 1
    if opt == 2:
        ans = int(input(str(num1)+" - "+str(num2)+"= "))
        if ans == num1 - num2:
            list.append((str(num1) + "-" + str(num2) + " = " + str(ans) + " (Correct) "))
            correct += 1
        else:
            list.append(
                (str(num1) + "-" + str(num2) + "= " + str(ans) + " (Incorrect) Correct answer is " + str(num1 - num2)))
        i += 1
    if opt == 3:
        ans = int(input(str(num1)+" * "+str(num2)+" = "))
        if ans == num1 * num2:
            list.append((str(num1) + "*" + str(num2) + "= " + str(ans) + " (Correct) "))
            correct += 1
        else:
            list.append(
                (str(num1) + "*" + str(num2) + " = " + str(ans) + " (Incorrect) Correct answer is " + str(num1 * num2)))
        i += 1
    if opt == 4:
        ans = int(input(str(num1)+" / "+str(num2)+"= "))
        if ans == num1 / num2:
            list.append((str(num1) + "/" + str(num2) + "= " + str(ans) + " (Correct) "))
            correct += 1
        else:
            list.append(
                (str(num1) + "/" + str(num2) + " = " + str(ans) + " (Incorrect) Correct answer is " + str(num1 / num2)))
        i += 1
for i in list:
    print(i)

print("Result : "+str(correct)+"%")