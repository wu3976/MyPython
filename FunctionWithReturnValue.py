#function could return value
def cube(num): #do not require specifying return type
    return num*num*num
    #print ("hh") never able to reach here because of return statement

result=cube(4) #pass actual parameter 4 into function cube, return 64, and assign this value to result
print(result)