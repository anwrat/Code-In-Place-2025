def main():
    a = "Anwesh"
    print(f"The string is {a}")
    print(f"The length of string is {len(a)}")
    print(f"The first letter is {a[0]}")
    print(f"The last letter is {a[-1]}")
    print(f"Slicing 1:4 : {a[1:4]}")
    print(f"Slicing from 1 to last element : {a[1:]}")
    print(f"Slicing from 0 to 3 : {a[:4]}")


if __name__ == '__main__':
    main()