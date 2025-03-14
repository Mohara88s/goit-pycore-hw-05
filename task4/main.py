from utility import parse_input, add_contact, change_contact, show_phone, show_all, colorize_message
from colorama import Fore, init
init(autoreset=True)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input(f"Enter a command: {Fore.LIGHTCYAN_EX}")
        print(Fore.RESET, end="")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(colorize_message(f"{"Name":<20}{"Phone":<15}", "MAGENTA"))
            for i, contact in enumerate(show_all(contacts)):
                print(colorize_message(f"{contact[0]:<20}{contact[1]:<15}", f"{"CYAN" if i%2==0 else "BLUE"}"))
        else:
            print(colorize_message("Invalid command.", "YELLOW"))

if __name__ == "__main__":
    main()
