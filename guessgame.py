# learning while loop in practice using  a guess game

secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter your guess (between 1 and 10): "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations! You've guessed the correct number.")
        break
else:
    print("Sorry, you've used all your attempts. The correct number was", secret_number)
