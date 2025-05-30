def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    correct = 0
    for key,value in translations.items():
        user = input(f"What is the Spanish translation for {key}? ")
        if(user == value):
            print("That is correct!")
            correct +=1
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {value}.")
        print()
    print(f"You got {correct}/{len(translations)} words correct, come study again soon!")


if __name__ == '__main__':
    main()