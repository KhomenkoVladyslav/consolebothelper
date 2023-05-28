USERS = {}


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "User not found"
        except ValueError:
            return "Give me your name and phone please"
        except IndexError:
            return "Enter user name"

    return inner


def hello_user(_):
    return "How can I help you?"


def unknown_command(_):
    return "unknown_command"


def exit(_):
    return


@error_handler
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f"User {name} added!"


@error_handler
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"{name} має новий телефон: {phone} Старий номер: {old_phone}"


def show_all(_):
    result = ""
    for name, phone in USERS.items():
        result += f"Name: {name} phone: {phone}\n"
    return result


@error_handler
def show_phone(args):
    name = args[0]
    if name in USERS:
        phone = USERS[name]
        return f"Phone number for {name}: {phone}"
    else:
        return "User not found"


HANDLERS = {
    "hello": hello_user,
    "add": add_user,
    "change": change_phone,
    "show all": show_all,
    "exit": exit,
    "good bye": exit,
    "close": exit,
}


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.lstrip()

    try:
        handler = HANDLERS[command.lower()]
    except KeyError:
        if args:
            command = command + " " + args[0]
            args = args[1:]
        handler = HANDLERS.get(command.lower(), unknown_command)
    return handler, args


def main():
    while True:
        user_input = input("Please enter command and args: ")
        handler, *args = parse_input(user_input)
        result = handler(*args)
        if not result:
            print("Exit")
            break
        print(result)


if __name__ == "__main__":
    main()
