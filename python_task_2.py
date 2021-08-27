import random
print("||       //\\      ||  ||=======  ||        ||======== ||=========||  ||\      /||  ||========    \n")
print("||      //  \\     ||  ||         ||        ||         ||         ||  || \    / ||  ||            \n")
print("||    //     \\    ||  ||         ||        ||         ||         ||  ||  \  /  ||  ||            \n")
print("||   //       \\   ||  ||=====    ||        ||         ||         ||  ||   \/   ||  ||=====       \n")
print("||  //         \\  ||  ||         ||        ||         ||         ||  ||        ||  ||            \n")
print("|| //           \\ ||  ||         ||        ||         ||         ||  ||        ||  ||            \n")
print("||//             \\||  ||======== ||======= ||======== ||=========||  ||        ||  ||========    \n")


# 1(Generate random Input)
def randomIn():
    n = random.randint(1000, 10000)
    # print("The random integer is %d" % n)
    return n


# 2(Taking user Input)
def UserIn():
    print("-----------------------------------------------------------------------")
    n = input("Input a 4 digit integer: ")
    return n


# 3(change integer to list)
def Int_to_list(a):

    integer = int(float(a))
    digit_string = str(integer)
    digit_map = map(int, digit_string)
    global digit_list
    digit_list = list(digit_map)

    return digit_list


# 4(Find the digits common between two lists)
def common_digit_list(lst1, lst2):

    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


# 5(Find the no. of correct matches)
def correct_matches(a, b):
    matches = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            matches += 1
    return matches


# 6(Printing the correct matches,correct position,Wrong position count )
def printOut(lst_rand, lst_user):

    list1 = common_digit_list(lst_user, lst_rand)

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


# 7(This func decides the num is equal to the random number or not .)
def decide(num, user_input, score, lst_rand, lst_user, Turns):
    flag = 0

    if(str(num) == str(user_input) and correct_matches(lst_rand, lst_user) == 4):

        print("\nAll digits are in the correct places.")
        print("You have won the game!!\n\n")
        print("Score = ", score)
        print("-------------------------------------------------------------")
        flag = 1
    else:

        printOut(lst_rand, lst_user)
        if(Turns != 0):
            print("\nTurns remaining- ", Turns)
        else:
            print("\nYou lose the game!\n")
            print("-------------------------------------------------------------")
    return flag


# 8(This function is the working part of main and taking turns and process it.)
def working(Turns, num, lst_rand, score):

    while(Turns >= 1):

        Turns -= 1

        user_input = UserIn()
        while(len(user_input) != 4):
            user_input = UserIn()
        lst_user = Int_to_list(str(user_input))

        print("\nOutput-\n")
        print("The user list is ", lst_user)

        # The below code block find the score according to the user input.
        if(Turns == 9):
            p_lst = common_digit_list(lst_user, lst_rand)
            score = 7*len(p_lst)-8
        else:
            correct_digit_lst = common_digit_list(lst_user, lst_rand)
            count = 0
            for i in range(len(correct_digit_lst)):
                Marker = 0
                for j in range(len(p_lst)):
                    if(correct_digit_lst[i] == p_lst[j]):
                        p_lst[j] = -2
                        Marker = 1
                        break
                if(Marker == 0):
                    count += 1

            score += (5*count)+2*len(correct_digit_lst)-8
            p_lst = correct_digit_lst

            # Till this the score block.

        print("\Your score is = ", score)
        flag = decide(num, user_input, score, lst_rand, lst_user, Turns)

        if(flag == 1):
            break


# 9(this func is for restart the game)
def restart_game():

    restart = input("Do you want to play again?(yes/no):\n>>").lower()
    if restart == "yes":
        main()

    else:
        exit()


# 10(This the main function for run our code)
def main():
    num = randomIn()
    lst_rand = Int_to_list(num)

    Turns = 10
    score = 0

    working(Turns, num, lst_rand, score)
    print("\n\n")
    restart_game()


# Calling of main function
main()
