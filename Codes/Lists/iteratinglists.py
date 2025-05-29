def main():
	my_list = [11,13,12,99]
	print("Using for range len loop")
	for i in range(len(my_list)):
		print(my_list[i])
	print("Using for element loop")
	for elem in my_list:
		print(elem)

if __name__ == '__main__':
	main()