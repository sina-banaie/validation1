import re



def name_checker(name):
    if re.match(r"^[a-zA-Z\s]$",name):
        print("valid")
        return True
    else:
        print("invalid")
        return False

def email_checker(email):
    if re.match (r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z{2,}]$",email):
        print("valid")
        return True
    else:
        print("invalid")
        return False

def family_checker(family):
    if re.match(r"^[a-zA-Z\s]$",family):
        print("valid")
        return True

    else:
        print("invalid")
        return False

def nationalcode_checker(national_code):
    if re.match(r"^[0-9]{6,15}$",national_code):
        print("valid")
        return True
    else:
        print("invalid")
        return False

def postalcode_checker(postalcode):
    if re.match(r"^[0-9]{4,15}$",postalcode):
        print("valid")
        return True
    else:
        print("invalid")
        return False

def mobile_checker(mobile):
    if re.match(r"^0[0-9]{11}$", mobile):
        print("Valid")
        return True
    else:
        print("invalid")
        return False