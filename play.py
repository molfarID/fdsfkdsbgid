from game import TrueFalse

start_game = input("Enter 'y' for start game or other latter for leave: ")
games = TrueFalse()
if start_game.lower() == "y":
    while games.sproby >= 1:
        print(games.give_question())
        select_q = games.result_reply(input("Enter reply: "))
        print(select_q)
        if games.len_quest == games.true_quest:
            print("You WIN!")
            break
    else:
        print("You LOSE!")
else:
    print("Goodbye!")


# print(game.TrueFalse.play())
