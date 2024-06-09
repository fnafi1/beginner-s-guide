import hashlib

data = input("enter the string to hash: ")

hash_object = hashlib.sha256(data.encode())

hex = hash_object.hexdigest()

with open("hash_values.txt", "w") as file:
    file.write(f"entered string: {data}\n")
    file.write(f"SHA-256 hash: {hex}\n")

print("the values were successfully written to the file 'hash_values.txt'")

