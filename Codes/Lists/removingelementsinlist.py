def main():
	my_list = [11,13,12,99,11]
	print(f"Original List: {my_list}")
	removed = my_list.pop(2) # Removes the index 2 element
	print(f"List after removing index 2 element: {my_list}")
	# remove method removes the first instance of element from the list
	my_list.remove(11)
	print(f"List after removing 11: {my_list}")

if __name__ == '__main__':
	main()