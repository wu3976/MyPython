lucky_numbers=[4, 8, 15, 16, 23, 42]
friends=["Kevin", "Karen", "Jim", "Oscar", "Tim", "Jim"]
friends.extend(lucky_numbers) #append lucky_numbers list to end of the friends list
print (friends)

friends.append("Me") # append me to the end of the list
print(friends)
friends.insert(1, "gg") #insert "gg" to the index 1 position, all the values pushed right
print (friends)
friends.remove("Jim") #remove the first "Jim" element in the list
print(friends)
friends.clear() #remove all the elements
print(friends)

friends=["Kevin", "Karen", "Jim","Oscar", "Tim","Jim"]
friends.pop() #remove the last element in the list
print(friends)

i=friends.index("Jim") #find the index of first "Jim" in the list. If not in the list, throws error.
print(i)

count=friends.count("Jim") #count the element with value "Jim"
# (problem: when "Jim"s are not together, it would only count 1. Maybe it only allow 1 element between them)
print(count)

friends.sort() #sort by alphabetic order
print(friends)

lucky_numbers.sort() # sort in ascending order
print(lucky_numbers)

lucky_numbers.reverse() #reverse the list
print(lucky_numbers)

friends2=friends.copy() #copy the value of list friends and give it to friends2
print(friends2)