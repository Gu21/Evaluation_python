# _*_ coding:Utf8 _*_

from controller.History_actions import get_history, drop_history
from controller.maze_solving import select_map, solve_maze


# Display resolution history
def display_history():
    rows = get_history()

    # For each row in the database, display the object's attributes
    for row in rows:
        print(row.read_history())


# Display the solution of a random unsolved map
def display_maze_solved():
    # Select a random map
    file = select_map()

    # Solve the maze
    lab, solving_time = solve_maze(file)

    # Print the solution
    for i in range(lab.ny):
        for j in range(lab.nx):
            if (i, j) in lab.path:
                print(".", end="")
            else:
                print(lab.lab[i][j], end="")

        print()
    print("Execution time: ", solving_time)


# Display the selection menu
def menu():
    # Menu display
    print("THE MAZE\n\n1- Show history\n2- Solve a maze\n3- Quit\n")

    while True:
        try:
            player_choice = int(input(f"\nSelect an option: "))

            match player_choice:
                # Display resolution history
                case 1:
                    display_history()

                # Solve a random maze
                case 2:
                    display_maze_solved()

                # Exit
                case 3:
                    exit(0)

                # Drop table (for purpose test only)
                case 9:
                    drop_history()

                # Other cases
                case other:
                    print("Incorrect choice, enter a number between 1 and 3")

        # If the user's choice isn't a number
        except ValueError as v:
            print("Incorrect choice, enter a number between 1 and 3")
            print(v)

        # If an exception is raised
        except Exception as e:
            print(f"Error : {e}")


# This code is executed only if this file is the start of the program
if __name__ == "__main__":
    menu()
    exit(0)
