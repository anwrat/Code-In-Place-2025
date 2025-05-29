def main():
	my_list = [11,13]
	print(f"List before appending: {my_list}")
	my_list.append(34) #Append element to end of list
	print(f"List after appending: {my_list}")
	x = my_list.pop()
	print(f"Last element is {x}")
	print(f"List after popping: {my_list}")

	#Extending list by making a new list
	a = [2,4,6]
	print(f"Before Extending: {a}")
	b=[8,10,12]
	combined = a+b
	print(f"The combined list is {combined}")

	#Extending a list by combining to one list
	a.extend(b)
	print(f"After Extending: {a}")

	#Getting index of first instance of element
	x = [1,2,1,3,4,1]
	print(f"The list is {x}")
	indexof1 = x.index(1)
	print(f"The index of first instance of 1 is {indexof1}")

	#Inserting elements
	x.insert(2,6)
	print(f"List after insetring 6 to index2 is {x}")


if __name__ == '__main__':
	main()