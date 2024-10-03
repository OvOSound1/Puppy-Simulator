# Names: Francisco Fausto, Tiffany Nguyen, Nick Breeding
# Assignment: Lab 13, Group 7
# Course: CECS 277 Sec 04
# Date: May 9th, 2024
# Desc: Using the State pattern, I'm developing a puppy simulator where the puppy's reactions to feeding or playing vary depending on its current state among asleep, eating, or playing

from puppy import Puppy

def main():
    """
    Main function to simulate interactions with a virtual puppy.
    """
    print("Congratulations on your new puppy!")
    puppy = Puppy()  # Create a new instance of the Puppy class

    while True:
        print("What would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            puppy.give_food()  # Call the give_food method of the Puppy instance
        elif choice == 2:
            puppy.throw_ball()  # Call the throw_ball method of the Puppy instance
        elif choice == 3:
            print("\nGoodbye!")
            break  # Exit the loop if the user chooses to quit
        else:
            print("\nInvalid choice. Please choose a number between 1 and 3.")

if __name__ == "__main__":
    main()
