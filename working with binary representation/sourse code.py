def encode():
    try:
        number = int(input("enter the number: "))
        binary = bin(number)
        with open("binary.txt", "w") as file:
            file.write(f"binary representation of a number {number}: {binary}\n")
        print(f"data is saved in the file binary.txt")
    except ValueError:
        print("error enter an integer")

encode()
