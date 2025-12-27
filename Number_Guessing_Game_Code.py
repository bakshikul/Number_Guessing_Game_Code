import random
def number_guessing_game():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    print(f"Guess the number between {lower_bound} and {upper_bound}")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print("Out of range. Try again.")
            elif guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    number_guessing_game()
