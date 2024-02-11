def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input format. Please provide both name and phone number."
        except Exception:
            return "An error occurred. Please try again."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone_number = args
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return f"\n{name}'s phone number: {contacts[name]}"
    else:
        return "Contact not found."

@input_error
def show_all_contacts(contacts):
    if contacts:
        result = "All contacts:"
        for name, phone_number in contacts.items():
            result += f"\n{name}: {phone_number}"
        return result
    else:
        return "Phonebook is empty."
