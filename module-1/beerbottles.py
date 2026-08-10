"""Module for counting down bottles of beer on the wall.

Name: [Your Name]
Date: [Insert Date]
Assignment: Module 1 Assignment - Beer Bottles Countdown
Purpose: Prompts the user for a starting bottle count with error handling,
prints the "Bottles of Beer" lyrics, and prompts the user to run again.
"""


def countdown(bottles):
    """Count down from starting bottles to 1 and print song lyrics."""
    current = bottles

    while current > 0:
        if current == 1:
            print(
                f"{current} bottle of beer on the wall, "
                f"{current} bottle of beer."
            )
        else:
            print(
                f"{current} bottles of beer on the wall, "
                f"{current} bottles of beer."
            )

        remaining = current - 1
        print(
            "Take one down and pass it around, "
            f"{remaining} bottle(s) of beer on the wall.\n"
        )

        current = current - 1


def main():
    """Manage user input, countdown execution, and program restart."""
    while True:
        while True:
            try:
                num_bottles = int(input("Enter number of bottles:"))
                if num_bottles > 0:
                    break
                print("Error: Please enter a whole number greater than 0.\n")
            except ValueError:
                print("Error: Invalid input. Please enter a whole number.\n")

        countdown(num_bottles)

        print("Time to buy more bottles of beer.\n")

        again = input("Would you like to try again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
