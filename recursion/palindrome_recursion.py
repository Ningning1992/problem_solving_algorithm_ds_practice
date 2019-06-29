def removeWhite(s):
    s_new = ''.join(c for c in s if c.isalnum())
    return s_new

def isPal(s):
    s = removeWhite(s)
    if len(s) == 1:
        return True
    elif len(s) == 0:
        return True
    else:
        if s[0] == s[-1]:
            return isPal(s[1:-1])
        else:
            return False


assert isPal(removeWhite("x"))==True
assert isPal(removeWhite("radar")) == True
assert isPal(removeWhite("hello")) == False
assert isPal(removeWhite("")) == True
assert isPal(removeWhite("hannah")) == True
assert isPal(removeWhite("madam i'm adam")) == True




