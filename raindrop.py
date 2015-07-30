__author__ = 'iAntoine'
import random
import time

def main():
    print("Welcome to Raindrop Game!")

    mistake = 3
    score=0
    totalQuestion = 0

    start = time.time()

    while True:

        opChoice = ['+', '*', '-']
        op = opChoice[random.randint(0, 2)]

        if op == '-':
            b = random.randint(1, 12)
            a = random.randint(b, 12)
        else:
            a = random.randint(1, 12)
            b = random.randint(1, 12)

        print("{0} {1} {2}".format(a, op, b))
        userResponse = int(raw_input())

        if op == '+':
            resultForPlus = a + b
            if not(userResponse == resultForPlus):
                mistake -= 1
		print("NOOOOO")
            else:
                print("OK")
                score += 1
        elif op == '-':
            resultForMinus = a - b
            if not(userResponse == resultForMinus):
                mistake -= 1
		print("NOOOOO")
            else:
                print("OK")
                score += 1
        elif op == '*':
            resultForCross = a * b
            if not(userResponse == resultForCross):
                mistake -= 1
		print("NOOOOO")
            else:
                print("OK")
                score += 1

        totalQuestion += 1

        if mistake <= 0:
            stop = time.time()
            print("You've done: {0} / {1}".format(score, totalQuestion))
            Gametime = stop - start
            print("Time: {} sec".format(int(Gametime)))
            print("Equation per minute: {}".format(score*60 / Gametime))
            break

if __name__ == "__main__":
    main()
