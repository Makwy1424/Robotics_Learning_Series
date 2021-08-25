import random
print("||       //\\      ||  ||=======  ||        ||======== ||=========||  ||\      /||  ||========    \n")
print("||      //  \\     ||  ||         ||        ||         ||         ||  || \    / ||  ||            \n")
print("||    //     \\    ||  ||         ||        ||         ||         ||  ||  \  /  ||  ||            \n")
print("||   //       \\   ||  ||=====    ||        ||         ||         ||  ||   \/   ||  ||=====       \n")
print("||  //         \\  ||  ||         ||        ||         ||         ||  ||        ||  ||            \n")
print("|| //           \\ ||  ||         ||        ||         ||         ||  ||        ||  ||            \n")
print("||//             \\||  ||======== ||======= ||======== ||=========||  ||        ||  ||========    \n")


def randomIn():
    n = random.randint(1000, 10000)

    return n


def UserIn():
    print("-----------------------------------------------------------------------")
    n = input("Input a 4 digit integer: ")
    return n

# digit_list = []


def Int_to_list(a):

    try:
        integer = int(float(a))
        digit_string = str(integer)
        digit_map = map(int, digit_string)
        global digit_list
        digit_list = list(digit_map)
    except ValueError:
        pass

    return digit_list


def common_digit_list(a, b):
    a_set = set(a)
    intersection = a_set.intersection(b)

    intersection_list = list(intersection)
    return intersection_list


def correct_matches(a, b):
    matches = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            matches += 1
    return matches


def printOut(lst_rand, lst_user):

    list1 = common_digit_list(lst_rand, lst_user)
    correct_number = len(list1)
    correct_position = correct_matches(lst_rand, lst_user)
    wrong_position = correct_number-correct_position

    if(len(list1) != 0):
        print(correct_number, "digits: ", list1, "gussed correctly")
        if(correct_position != 0):
            print(correct_position, "in the correct position.")
        if(wrong_position != 0):
            print(wrong_position, "in the wrong position.")
    else:
        print("U don't guess a right digit!Try your best for the next round\n")


def working(Turns, num, lst_rand, score):

    while(Turns >= 1):

        Turns -= 1

        user_input = UserIn()
        while(len(user_input) != 4):
            user_input = UserIn()

        lst_user = Int_to_list(str(user_input))
        print("\nOutput-\n")
        print("The user list is ", lst_user)
        if((str(num) == user_input) and (correct_matches(lst_rand, lst_user))):
            score += 5
            print("\nAll digits are in the correct places.")
            print("You have won the game!!\n\n")
            print("Score = ", score)
            print("-------------------------------------------------------------")

            break
        else:
            score -= 2
            printOut(lst_rand, lst_user)
            if(Turns != 0):
                print("\nTurns remaining- ", Turns)
            else:
                print("\nYou lose the game!\n")
                print("-------------------------------------------------------------")


def restart_game():

    restart = input("Do you want to play again?(yes/no):\n>>").lower()
    if restart == "yes":
        main()

    else:
        exit()


def main():
    num = randomIn()
    lst_rand = Int_to_list(num)
    Turns = 10
    score = 20

    working(Turns, num, lst_rand, score)
    print("\n\n")
    restart_game()


# Calling of main function
main()
