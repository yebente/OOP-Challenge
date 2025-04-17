import pet
import time
# This is a simple pet simulator program that allows users to create a pet and interact with it.
# The user can feed the pet, play with it, teach it tricks, and check its status.
# The program uses a class to represent the pet and its attributes, and it provides a simple text-based interface for user interaction.
# The program is designed to be easy to use and understand, making it suitable for beginners in programming.
# The program is written in Python and uses basic programming concepts such as classes, methods, and user input.
# The program is designed to be run in a terminal or command prompt, and it provides clear instructions for the user to follow.

def loading(action, petName=""):
    """Simulate loading time for pet actions."""
    if action == "teach":
        print(f"Teaching {petName} the new trick", end="")
    else:
        print(f"{petName} is {action}ing", end="")
    for i in range(3):
        print(".", end="")
        time.sleep(1)
    time.sleep(2) 
    print("\n")

# Main program starts here
print("==============================================")
print("Welcome to the Pet Simulator!")
print("You can create a pet and interact with it.")
print("Let's get started!")
name = input("Please enter the name of your pet: ")

userPet = pet.Pet(name)
print("==============================================")
print(f"Congratulations! You have created a pet named {userPet.name}.")
print("==============================================")
print("Now, let's see what you can do with your pet.")

while True:
    print("Available options:")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Teach your pet a trick")
    print("4. Check your pet's status")
    print("5. Exit")
    print("==============================================")
    try:
        userChoice = int(input("Please choose an option (1-5):"))
        if userChoice < 1 or userChoice > 5:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        print("==============================================")
        time.sleep(2)  # Adding a delay for better readability


    # Processing user choice
    if userChoice == 1:
        loading("feed", userPet.name)
        # Simulate feeding the pet
        status = userPet.feed()
        # print("Your pet has been fed.") #add in feed method
    elif userChoice == 2:
        loading("play", userPet.name)
        # Simulate playing with the pet
        userPet.play()
    elif userChoice == 3:
        trick = input("Please enter the trick you want to teach your pet: ")
        loading("teach", userPet.name)
        userPet.teach_trick(trick)
        # print(f"You taught your pet the trick: {trick}.") #add in feed method
    elif userChoice == 4:
        print(userPet.get_status())
    elif userChoice == 5:
        print("Thank you for using the Pet Simulator!")
        break
    else:
        print("Invalid choice. Please try again.")
        print("==============================================")
# Simulate closing the simulator
print("Closing the Pet simulator", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)          
