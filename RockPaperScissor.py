import random
print("1.Rock\n2.Paper\n3.Scissors\n---------------------------------")   
def main():
    User = int(input("Enter Your Choice"))
    Computer = random.randint(1,3)
    if User==1:
        print("You Choose Rock ðª¨")
        if Computer==1:
            print("Computer Choose Rock ðª¨\nThis is Draw")
        elif Computer==2:
            print("Computer Choose Paper ð\nYou Loseðð¤ª")
        elif Computer==3:
            print("Computer Choose Scissors âï¸\nYou Win ð¥³ð¥³ð")
    elif User==2:
        print("You Choose Paper ð")
        if Computer==2:
            print("Computer Choose Paper ð\nThis is Draw")
        elif Computer==3:
            print("Computer Choose Scissors âï¸\nYou Loseðð¤ª")
        elif Computer==1:
            print("Computer Choose Rock ðª¨\nYou Win ð¥³ð¥³ð")
    elif User==3:
        print("You Choose Scissors âï¸")
        if Computer==3:
            print("Computer Choose Scissors âï¸\nThis Draw")
        elif Computer==1:
            print("Computer Choose Rock ðª¨\nYou Loseðð¤ª")
        elif Computer==2:
            print("Computer Choose Paper ð\nYou Win ð¥³ð¥³ð")
main()
