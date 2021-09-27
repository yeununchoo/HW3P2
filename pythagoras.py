print("Hello World,")
print("Welcome to my Pythagoras project!")

def is_acute(a,b,c):
    if a**2 + b**2 > c**2:
        return True
    else:
        return False

def is_obtuse(a,b,c):
    if a**2 + b**2 < c**2:
        return True
    else:
        return False