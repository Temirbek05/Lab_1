import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    while True:
        guess = input("Take a guess.\n")

        guess = int(guess)

        attempts += 1

        if guess == secret_number:
            print(f"Good job, KBTU! You guessed my number in {attempts} guesses.")
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

if __name__ == "__main__":
    guess_the_number()
