#create a Tuple
coord=(4, 5) #construct a tuple of coordinate
#cannot make change to the tuple

print(coord[0]) #print element of coord at index 0
#coord[0]=10 this code would generate a error

#difference of list and tuple:
#generally used in case when data that don't want to be changed

coords=[coord, (50, 25)]
print(coords)
coords[1]=(40, 30) #you can change an coordinate as a whole, bu could not make change inside each coordinate
print(coords)
