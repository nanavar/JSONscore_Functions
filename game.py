import random
import json
import datetime
from functions import game

name = input("What's your name? ")

date = datetime.datetime.now()
print(date)

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player": name, "secret_number": secret, "wrong_guesses": wrong_guesses})

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

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection == "A":
        print("-> Restarting game...")
        game()
    elif selection == "B":
        for score_dict in score_list:
            score_list = sorted(score_list, key=lambda k: k["attempts"])
            score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}.".format(score_dict.get("player"),
                                                                                                                              score_dict.get("attempts"),
                                                                                                                              score_dict.get("date"),
                                                                                                                              score_dict.get("secret_number"),
                                                                                                                              score_dict.get("wrong_guesses"))
            print(str(score_text))
    else:
        break