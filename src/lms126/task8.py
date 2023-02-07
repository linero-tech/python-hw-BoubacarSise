
def task8():
    return """
    INPUT X
    IF X MOD 3 = 0 AND X MOD 5 = 0
    OUTPUT "FooBar"
    ELSE 
    IF X MOD 3 = 0
    OUTPUT "Foo"
    ELSE 
    IF X MOD 5 = 0
    OUTPUT "Bar"
    ELSE
    OUTPUT "Qix"
    """
