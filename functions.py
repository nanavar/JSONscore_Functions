import random
import json
import datetime

#   GAME LVL EASY

def easy_game():
    secret = random.randint(1, 30)

    attempts = 0

    name = input("What's your name? ")

    date = datetime.datetime.now()
    print(date)

    wrong_guesses = []

    score_list = scores()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player": name, "secret_number": secret,
                               "wrong_guesses": wrong_guesses})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

        wrong_guesses.append(guess)

#   GAME LVL HARD

def hard_game():
    secret = random.randint(1, 30)

    attempts = 0

    name = input("What's your name? ")

    date = datetime.datetime.now()
    print(date)

    wrong_guesses = []

    score_list = scores()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player": name, "secret_number": secret,
                               "wrong_guesses": wrong_guesses})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        else:
            print("Your guess is not correct. Try again.")

        wrong_guesses.append(guess)

#   SCORE LIST

def scores():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_scores():
    score_list = scores()
    return (sorted(score_list, key=lambda person: person['attempts']))[:3]