# This is the main Python file for the Text-Based Adventure Game project.
def adventure():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    choice = input("Which one do you take? (left/right): ").lower()

    if choice == "left":
        print("You enter a room filled with treasure!")
    elif choice == "right":
        print("A dragon attacks! Game over.")
    else:
        print("Invalid choice! Game over.")

adventure()
