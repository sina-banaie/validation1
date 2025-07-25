from my_madule import*


assert name_checker("sina") == True
assert name_checker("Arya") == True
assert name_checker("sina130") == False
assert name_checker("") == False
assert name_checker("0-98") == False

assert family_checker("rezaie") == True
assert family_checker("Alipour") == True
assert family_checker("amiri890") == False
assert family_checker("") == False
assert family_checker("567") == False

assert nationalcode_checker("123456") == True
assert nationalcode_checker("002567544") == True
assert nationalcode_checker("a123") == False
assert nationalcode_checker("") == False



assert postalcode_checker("1234567") == True
assert postalcode_checker("456987567") == True
assert postalcode_checker("a123") == False
assert postalcode_checker("") == False

assert mobile_checker("09212125847") == True
assert mobile_checker("09120237829") == True
assert mobile_checker("5036756876") == False
assert mobile_checker("") == False
assert mobile_checker("0921tughftr") == False


assert email_checker("sinabanaie20001@gmail.com") == True
assert email_checker("sina7908@gmail.com") == True
assert email_checker("sinaooojgmail.com") == False
assert email_checker("") == False
assert email_checker("8876") == False

print("test completed")




