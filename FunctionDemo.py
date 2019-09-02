# function could help organize the code and ease the maintenance of Python code

def say_hi(): #don't necessary to seperate the words by underscore.
    print("Hello user")#code considered inside the functions need to be indented
    print("I am Chenjie Wu")

#call the function
say_hi()

def say_hi2(name, age): #pass parameter name and age into function.
                        # does not need to specify formal parameter type
    print("Hello, "+name+", you are "+str(age)+" years old")

say_hi2("Chenjie", 19)