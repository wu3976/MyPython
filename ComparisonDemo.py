def max_num (num1, num2, num3): #find the largest number in these 3
    max=num1
    if num1>=num2:
        if num1>=num3:
            max=num1
        else:
            max=num3
    elif num2>=num3:
        max=num2
    else:
        max=num3
    return max

print (max_num(5, 3, 7))

def is_equal (str1, str2): #compare if two string is equal
    return str1==str2 #in Python, object contents are compared using == instead of equals()
                    # != is "not equal"

print (is_equal("gg", "gg"))