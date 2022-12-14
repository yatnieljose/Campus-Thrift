from tkinter import messagebox


def validate_name(name):
    """Checks username integrity (between 6 and 16 characters)"""

    if len(name) < 6:
        messagebox.showinfo(title='UsernameTooShort',
                            message="Username is too short. Username must be between 6 and 16 characters.")
        return False

    if len(name) > 16:
        messagebox.showinfo(title="UsernameTooLong",
                            message="Username is too long. Username must be between 6 and 16 characters.")
        return False

    return True


def validate_email(email):
    """check email integrity (conforms to acceptable email format)"""

    # split into prefix and domain, separated by @
    # check if more than one @
    email_split = email.split("@")
    if len(email_split) != 2:
        email_failure_message()
        return False
    email_prefix = email_split[0]
    email_domain = email_split[1]

    # validate prefix by name length and type of characters allowed
    if not (1 <= len(email_prefix) <= 256):
        email_failure_message()
        return False

    # validate prefix ends with alphanumeric character
    if not email_prefix[-1].isalnum():
        email_failure_message()
        return False

    # validate every character in prefix is alphanumeric, underscore (_), period(.), or dash(-)
    for c in email_prefix:
        if not (c.isalnum() or c == '_' or c == '.' or c == '-'):
            email_failure_message()
            return False

    # split domain by .
    domain_split = email_domain.split(".")
    if (len(domain_split) != 2):
        email_failure_message()
        return False
    domain_prefix = domain_split[0]
    domain_suffix = domain_split[1]

    # validate domain prefix
    if not (1 <= len(domain_prefix) <= 64):
        email_failure_message()
        return False

    if not domain_prefix[-1].isalnum():
        email_failure_message()
        return False

    for c in domain_prefix:
        if not (c.isalnum() or c == "-"):
            email_failure_message()
            return False

    # validate domain suffix
    if not (1 <= len(domain_suffix) <= 64):
        email_failure_message()
        return False

    if not domain_suffix[-1].isalnum():
        email_failure_message()
        return False

    for c in domain_suffix:
        if not (c.isalnum() or c == "-"):
            email_failure_message()
            return False

    return True


def validate_password(password, confirm_pw):
    """Checks password integrity (between 6 and 64 characters)"""

    if len(password) < 6:
        messagebox.showinfo(title="WrongPasswordFormat",
                            message="Password must be at least 6 characters.")
        return False

    if len(password) > 64:
        messagebox.showinfo(title="LongPasswordFormat",
                            message="Password must be 64 characters maximum.")
        return False

    if password != confirm_pw:
        messagebox.showinfo(title="PasswordMismatchFormat",
                            message="Passwords do not match.")
        return False

    return True


def validate_bio(bio):
    """Checks bio integrity (256 character maximum)"""

    if len(bio) > 256:
        messagebox.showinfo(title="LongBioFormat",
                            message="Bio must be 256 characters maximum.")
        return False
    return True


def email_failure_message():
    """Displays a message box indicating that the email format is incorrect"""

    messagebox.showinfo(title="WrongEmailFormat",
                        message="Email format incorrect.")


def validate_is_number(user_input):
    """Validates whether a given user input is a positive integer"""

    try:
        val = int(user_input)
    except ValueError:
        messagebox.showinfo(title="NaN",
                            message="Input is not a number.")
        return False

    return True


def validate_offer(minimum_bid, highest_bid, user_input):
    """Validates a user input against the current highest bid for an item"""

    if not validate_is_number(user_input):
        return False

    user_input = int(user_input)

    if user_input < minimum_bid:
        messagebox.showinfo(title="LowerThanMin",
                            message="Offer must be at least equal to the minimum accepted bid.")
        return False
    if user_input <= highest_bid:
        messagebox.showinfo(title="LowerThanMax",
                            message="Offer must be greater than the current maximum")

    if user_input > highest_bid and user_input >= minimum_bid:
        return True
    else:
        messagebox.showinfo(title="Not enough",
                            message="Offer needs to be higher than current maximum.")
        return False
