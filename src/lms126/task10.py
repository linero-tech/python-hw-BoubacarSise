
def task10():
    return """
    INPUT email, password
    IF email already exist in the database
    OUTPUT "Email already exists. Please use another email."
    ELSE
    IF length of password < 6
    OUTPUT "Password must be at least 6 characters long."
    ELSE
    add_account(email, password)
    OUTPUT "Account creation successful. Welcome to our service."
    """
