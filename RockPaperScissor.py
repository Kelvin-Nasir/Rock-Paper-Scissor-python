import random
print("1.Rock\n2.Paper\n3.Scissors\n---------------------------------")   
def main():
    User = int(input("Enter Your Choice"))
    Computer = random.randint(1,3)
    if User==1:
        print("You Choose Rock 🪨")
        if Computer==1:
            print("Computer Choose Rock 🪨\nThis is Draw")
        elif Computer==2:
            print("Computer Choose Paper 📃\nYou Lose😛🤪")
        elif Computer==3:
            print("Computer Choose Scissors ✂️\nYou Win 🥳🥳🎉")
    elif User==2:
        print("You Choose Paper 📃")
        if Computer==2:
            print("Computer Choose Paper 📃\nThis is Draw")
        elif Computer==3:
            print("Computer Choose Scissors ✂️\nYou Lose😛🤪")
        elif Computer==1:
            print("Computer Choose Rock 🪨\nYou Win 🥳🥳🎉")
    elif User==3:
        print("You Choose Scissors ✂️")
        if Computer==3:
            print("Computer Choose Scissors ✂️\nThis Draw")
        elif Computer==1:
            print("Computer Choose Rock 🪨\nYou Lose😛🤪")
        elif Computer==2:
            print("Computer Choose Paper 📃\nYou Win 🥳🥳🎉")
main()
