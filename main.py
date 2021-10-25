from functions import easy_game, hard_game, get_scores

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection == "A":
        level = input("Do you want to play (easy/hard) mode? ")
        if level == "easy":
            easy_game()
        elif level == "hard":
            hard_game()
        else:
            print("Wrong input!")
    elif selection == "B":
        for score_dict in get_scores():
            score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}.".format( score_dict.get("player"),
                                                                                                                               score_dict.get("attempts"),
                                                                                                                               score_dict.get("date"),
                                                                                                                               score_dict.get("secret_number"),
                                                                                                                               score_dict.get("wrong_guesses"))
            print(str(score_text))
    else:
        break