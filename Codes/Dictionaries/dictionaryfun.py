def main():
	my_dict = {'Takumi':'Toyota AE86', 'Keisuke':'Mazda RX-7 FD', 'Ryosuke':'Mazda RX-7 FC', 'Shingo': 'Honda Civic EG6', 'Bunta':'Subaru Impreza WRX'}
	
    # Length of dictionary
	print(f"The length of dictionary is {len(my_dict)}")
	print("The cars are: ")
	i=1
	# Looping using values
	for values in my_dict.values():
		print(str(i)+". "+values)
		i+=1
	# Looping using keys
	for key in my_dict.keys():
		print(f"{key} drives a {my_dict[key]}")
	i=1
	# Looping using items
	for key, values in my_dict.items():
		print(f"{i}. {key} -> {values}")
		i+=1
    # Removing a key and value pair
	removed = my_dict.pop('Bunta')
	print(f"Dictionary after removal is {my_dict} \nThe removed value is {removed}")
	
    # Del function, it doesnot return a value like pop
	del my_dict['Shingo']
	print(f"After using the del function: {my_dict}")

    # Clear the dicitonary
	my_dict.clear()
	print(f"After clearing, the dict is {my_dict}")
if __name__ == '__main__':
	main()