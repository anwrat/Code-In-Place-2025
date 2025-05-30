def main():
	my_dict = {'Takumi':'Toyota AE86', 'Keisuke':'Mazda RX-7 FD', 'Ryosuke':'Mazda RX-7 FC', 'Shingo': 'Honda Civic EG6', 'Bunta':'Subaru Impreza WRX'}
	for key in my_dict:
		print(f"{key} drives a {my_dict[key]}")

if __name__ == '__main__':
	main()