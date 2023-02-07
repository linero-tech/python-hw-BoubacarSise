
def task11():
    return """
    INPUT temperature
    IF temperature ends with "C"
    temperature = temperature without "C"
    temperature = (temperature * 9 / 5) + 32
    OUTPUT temperature + "F"
    ELSE IF temperature ends with "F"
    temperature = temperature with "F"
    temperature = (temperature - 32) * 5 / 9
    OUTPUT temperature + "C"
    """
