# terminal_game.py
import random

def main():
    print("Welcome to another Universe of Aliens!")
    print("You wake up on a new planet to a strange noise...")
    choice1 = input("Do you (1) check on the noise or (2) hide under the rocks? ")

    if choice1 == "1":
        print("You see a group of aliens!")
        fight_or_run = input("Do you (1) fight or (2) run and report it to Earth? ")

        if fight_or_run == "1":
            if random.randint(1, 10) > 5:
                print("You bravely fight off the aliens and come back to Earth as a hero!")
            else:
                print("The alien defeats you. You lose!")
        else:
            print("You survive for now, but later you get caught by aliens.")

    elif choice1 == "2":
        print("You hide there for days and you get hungry and thirsty.")
        print("Suddenly, you decide to come out of the rocks and you have two choices:")
        print("1) Start searching for food")
        print("2) Wait for rescue")
        choice2 = input("What do you want to do? ")

        if choice2 == "1":
            print("You search for food and find some alien fruits. They look terrible!")
            fruit_choice = input("Would you eat them? (1) Yes (2) No ")

            if fruit_choice == "1":
                if random.randint(1, 10) > 3:
                    print("The fruits are delicious! You survive and thrive on the new planet, and eventually you win.")
                else:
                    print("The fruits were poisonous! You lose!")
            else:
                print("You don’t eat the fruits and eventually starve. You lose!")
        elif choice2 == "2":
            print("You wait for rescue, but no one comes. You eventually starve and lose.")
        else:
            print("Invalid choice. Game over.")
    else:
        print("Invalid choice. Game over.")

if __name__ == "__main__":
    main()
