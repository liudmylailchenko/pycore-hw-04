def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    try:
        name, phone = args
    except ValueError:
        return "Please enter name and phone"

    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    try:
        name, phone = args
    except ValueError:
        return "Please enter name and phone"
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found"


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    try:
        name = args
    except ValueError:
        return "Please enter name"

    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"


def show_all(contacts: dict[str, str]) -> str:
    return "\n".join(f"{contact}: {phone}" for contact, phone in contacts.items())


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
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
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
