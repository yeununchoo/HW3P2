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

def is_right(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def cos_angle(a, b, c):
    return (a**2 + b**2 - c**2)/(2*a*b)
