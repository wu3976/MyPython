#basic if-statement

is_male=True
is_tall=True

if is_male: #enter the branch if the boolean value in the parenthesis is true
    print("You are a male") #branch body need to be indented
else: #enter the else branch if all if-branch is not entered
    print("You are not a male")

if is_male or is_tall: #either one of the two value is true can lead to the entrance of this branch
    print("You are male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall: #both of the two value is true can lead to the entrance of this branch
    print("You are male and tall")
else:
    print("You are either not male or not tall or both")

if is_male and is_tall: #both of the two value is true can lead to the entrance of this branch
    print("You are male and tall")
elif is_male and not(is_tall): #same as else if statement and ! modifier
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and short")
