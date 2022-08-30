import random

def game(rand):
    no_of_attempts = 1

    while True:
        guess = int(input("Please enter a number: "))

        if guess == rand:
            print(f"You guessed it correctly in {no_of_attempts}")
            break
        elif guess > rand:
            print("Wrong guess! Lower number please")
            no_of_attempts += 1
        else:
            print("Wrong guess! Higher number please")
            no_of_attempts += 1

    return no_of_attempts

if __name__ == "__main__":
    try:
        while True:
            a = int(input("Enter the lower bound: "))
            b = int(input("Enter the upper bound: "))

            rand = random.randint(a, b)
            print("Player 1 play")
            player1 = game(rand)

            rand = random.randint(a, b)
            print("Player 2 play")
            player2 = game(rand)

            if player1 == player2:
                print("Draw")
            elif player1 < player2:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

            while True:
                again = input("Do you want to play again?(yes or no): ").lower()
                if again == "yes":
                    break
                elif again == "no":
                    quit()
                else:
                    print("Enter yes or no")
                    continue

    except Exception as e:
        print("Integers only!")
