from validations import validate_user_input

def user_choice(message):
    return validate_user_input("Enter your choice (1-5): ", "positive_num")
