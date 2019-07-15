import random, time
global n
n = 0
def ask_to_play_again():
    play_again = '_'
    while play_again[0].lower() != 'y' or play_again[0].lower() != 'n':
        play_again = input("Do you want to play again:>(Yes or No) ")
        if len(play_again) >= 1:
            if play_again[0].lower() == 'y':
                coin_flip()
                break
            elif play_again[0].lower() == 'n':
                print("Thank you for playing.")
                break
            else:
                print("\n"*50)
                print(f"you entered {play_again}")
                print("Please type yes or no")
        else:
            print("\n"*50)
            print(f"Please type yes or no")
            ask_to_play_again()

def coin_flip():
    print("\n"*100)
    def coin_flipping():
        global n
        aa = input("what you want to choose Heads or Tails:> ")
        i = random.choice(["Heads", "Tails"])
        if len(aa) >= 1:
            while aa[0].lower() == 'h' or aa[0].lower() == 't':
                if aa[0].lower() == i[0].lower():
                    if n < 10:
                        print(f"Oh WoW it's {i}")
                        print("You have won the toss :)")
                        print(f"your score:> {n}")
                        n += 1
                        ask_to_play_again()
                    else:
                        print(f"Oh WoW it's {i}")
                        print("You have won the toss :)")
                        print("\n" * 100)
                        print(f"YOUR_SCORE:> {n}")
                        print(f"You have played enough, it is requested to take rest")
                        print(f"The game will be paused for 1 minute")
                        time.sleep(60)
                        n -= 11
                        ask_to_play_again()
                    break
                elif aa[0].lower() != i[0].lower():
                    print(f"Oh NO it's {i}")
                    print("You lost the toss!")
                    print(f"your score:> {n}")
                    ask_to_play_again()
                    break
            else:
                print("please choose Heads or Tails")
                coin_flipping()
        else:
            print("please type Heads or Tails")
            coin_flipping()
    coin_flipping()
coin_flip()