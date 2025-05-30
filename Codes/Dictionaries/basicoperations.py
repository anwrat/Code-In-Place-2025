def main():
    dicta = {'Chris':31, 'Mehran':50}
    # Accessing element in dictionary
    print(dicta['Chris'])
    # Changing value in dictionary
    dicta['Mehran'] = 18
    print(dicta['Mehran'])
    if 'Mehran' in dicta:
        print('Mehran is present')
    if 'Karel' not in dicta:
         print('Karel not present')
    # Adding elements to dictionary
    phone = {}
    phone['Pat'] = 9123123123
    phone['Takumi'] = 91283123123
    phone['Bunta'] = None
    print(phone)


if __name__ == '__main__':
	main()