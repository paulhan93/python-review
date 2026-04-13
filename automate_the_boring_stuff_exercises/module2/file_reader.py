# Date: Apr. 12, 2026
# Author: Paul Han
# Write a function that reads a .txt file and prints each line numbered
# Wrap it in a try/except so it handles a missing file gracefully
# Write a function that appends a new line to a file

from pathlib import Path

def print_file_lines():
    print("[INFO] Printing contents of 'notes.txt' file...")
    try:
        notes_path = Path.cwd() / 'notes.txt'
        with open(notes_path, encoding='UTF-8') as f:
            lines = f.readlines()
        line_count = len(lines)
        # Print each line number and content
        for i in range(line_count):
            print(f"[{i+1:03d}]:", lines[i], end="")
    except FileNotFoundError:
        print(f"The 'notes.txt' file does not exist in the current directory")

def append_to_file():
    text = input("Enter text to append: ")
    notes_path = Path.cwd() / 'notes.txt'
    with open(notes_path, 'a', encoding='UTF-8') as f:
        f.write(text + '\n')
    print("[INFO] Note has been saved!")

def main():
    # Welcome message & menu
    print("""
    Welcome to Notes Manager!
    -------------------------
    1. View notes
    2. Add a note
    3. Quit
    """)

    # Prompt user input
    user_choice: int = 0
    while user_choice != 3:
        try:
            user_choice = int(input("Choose an option: "))
        except ValueError:
            print("Please ensure the input is a number")
            continue

        if user_choice == 1:
            print_file_lines()
        elif user_choice == 2:
            append_to_file()
        elif user_choice == 3:
            print("Goodbye!")
            return
        else:
            print("Please enter a valid entry (ie. 1)")


if __name__ == "__main__":
    main()
