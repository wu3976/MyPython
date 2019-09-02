#Key value pair
#create a dictionary

monthConversions={
    "Jan": "January", #associate abbreviation "Jan" to value "January"
    "Feb": "Feburary", #the key must be unique within one list
}

print(monthConversions["Jan"]) #Inside the [], type in one key, output the value. If key is invalid, throws error
print(monthConversions.get("a", "Not valid")) #also work, output None value if not corresponding value found, or output
#second parameter value if not found
