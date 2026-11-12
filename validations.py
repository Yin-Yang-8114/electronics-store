

def validate_user_input(message, valitaion_type):
    while True:
        user_input = input(message)
        if valitaion_type == "int":
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Please enter a valid integer")
        if valitaion_type == "str":
            if user_input.isalpha():
                return user_input
            else:
                print("Please enter a valid string")
        if valitaion_type == "positive_num":
            try:
                value = int(user_input)
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
        if valitaion_type == "positive_float":
            try:
                value = float(user_input)
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
        if valitaion_type == "not_empty":
            if user_input.strip() != "":
                return user_input
            else:
                print("Input cannot be empty")