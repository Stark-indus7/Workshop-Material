import random 

# def levels():
#     print("""Enter the difficulty:
#         1. Easy : numbers(1 to 6)
#         2. Normal : numbers(1 to 50)
#         3. Hard : numbers(1 to 100)
#         4. Impossible : numbers(1 to 1000)
#         5. Mat Karo Ye Wala : numbers(1 to 1000000)
#         6. Exit""")
#     num = 0
#     while True:
#         try:
#             level = int(input("Enter The Level : "))
#             if level == 6:
#                 print("Nhi Khelna")
#                 break
#             if level == 1:
#                 num = random.randint(1,6)
#                 return num
#             elif level == 2:
#                 num = random.randint(1,50)
#                 return num
#             elif level == 3:
#                 num = random.randint(1,100)
#                 return num
#             elif level == 4:
#                 num = random.randint(1,1000)
#                 return num
#             elif level == 5:
#                 num = random.randint(1,1000000)
#                 return num
#             else:
#                 print("Invalid Num")
#         except ValueError:
#             print("Invalid Values for the num")    
#     return num


            

# def game_check():
#     num = levels()
#     my_chance = 1
#     while my_chance < 8:
#         guess = int(input("Enter your guess : "))
#         if guess == num:
#             print(f"You Guessed it right in {my_chance}")
#             break
#         elif guess > num:
#             print("Guessed number is larger than 'Number' ")
#             my_chance += 1
#         elif guess < num:
#             print("Guessed number is smaller than the 'Number'")
#             my_chance += 1
#         else:
#             print("Invalid")
#             my_chance += 1
#     else:
#         print(f"You Lose the Number was : {num}")

# game_check()



# option = ["rock","paper","scissor"]


# chances = 1
# player_scores = 0
# computer_scores = 0
# while chances < 10:
#     computer_choice = random.choice(option)
#     player_choice = input("Enter your choice (rock/paper/scissor): ").lower()
#     if player_choice == computer_choice:
#         print("Tie!")
#         chances += 1
#     elif player_choice == "rock" and computer_choice == 'paper':
#         print("Computer win!")
#         computer_scores += 5
#         chances += 1
#     elif player_choice == 'paper' and computer_choice == 'scissor':
#         print("Computer win!")
#         computer_scores += 5
#         chances += 1
#     elif player_choice == 'scissor' and computer_choice == 'rock':
#         print("Computer win!")
#         computer_scores += 5
#         chances += 1
#     elif player_choice == "paper" and computer_choice == 'rock':
#         print("Player win!")
#         player_scores += 5
#         chances += 1
#     elif player_choice == 'scissor' and computer_choice == 'paper':
#         print("Player win!")
#         player_scores += 5
#         chances += 1
#     elif player_choice == 'rock' and computer_choice == 'scissor':  
#         print("Player win!")
#         player_scores += 5
#         chances += 1
#     else:
#         print("Invalid")    
# else:
#     if player_scores > computer_scores:
#         print("Player Won!")
#     elif player_scores == computer_scores:
#         print("Both Tied!")    
#     else:
#         print("Computer Won!")    
#     print(f"Player Score = {player_scores}")        
#     print(f"Computer Score = {computer_scores}")        


# import pyautogui as pg
# import time

# prompt = input("Enter your video : ")
# time.sleep(4)
# pg.hotkey("winleft","s")

# time.sleep(1)
# pg.typewrite("chrome",interval=0.5)

# time.sleep(1)
# pg.press('enter')

# time.sleep(2)
# pg.typewrite("youtube.com",interval=0.5)

# time.sleep(1)
# pg.press('enter')

# time.sleep(2)
# pg.hotkey('/')

# time.sleep(3)
# pg.typewrite(prompt,interval=0.5)

# time.sleep(2)
# pg.press('enter')
