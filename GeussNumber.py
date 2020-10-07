import random
print()
print("Здравствуйте в этой игре вам нужно загадать целое число." )
print("Оно должно быть в интервале от 0 до N. N вы выбираете сами.")
print()

def CheckAnswer(number):

    print()
    while True:
        checking = input(f"Вы загадали {number}?   Да : 0;  Мое число меньше : 1;  Мое число больше: 2. Ваш ответ: ")
        if checking.isdigit() and (checking == "0" or checking == "1" or checking == "2"):
            checking = int(checking)
            break
    if checking == 0:
        print()
        print("Ура! Победа!")
    return checking

while True:
    B = input("Вы загадали чилсо в пределах от 0 до N = ")
    if B.isdigit():
        B = int(B)
        break

N = random.randint(0, B + 1)
A = 0
while True:
    CheckIt = CheckAnswer(N)
    if CheckIt == 0:
        break
    elif CheckIt == 1: # Нужно Меньше
        B = N
        if B - A == 0:
            print("")
            print(f"Вы сказали, что число больше {A-1} но меньше {B}, значит вы загадали {float(N)/2} но по условию вы должны были загадать целое число. Не надо недооценивать меня! ")
            print("")
            print("Ура, я победил!")
            break
        N = int((A+B)/2)
    elif CheckIt == 2: # Нужно больше
        A = N+1
        if B - A == 0:
            print("")
            print(f"Вы сказали, что число больше {A-1} но меньше {B}, значит вы загадали {float(N)/2} но по условию вы должны были загадать целое число. Не надо недооценивать меня! ")
            print("")
            print("Ура, я победил!")
            break
        N = int((A+B)/2)



