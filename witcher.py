print("Hello, stranger.")
name = input("What is your name?\n")
print(f"Hello, {name}.")

with open("Save", "w") as fd:
    fd.write(name)
