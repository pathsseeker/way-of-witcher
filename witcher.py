import sh

save = sh.find('.', '-type', 'f', '-name', 'Save').rstrip('\n')
if not save:
    print("Hello, stranger.")
    name = input("What is your name?\n")
    print(f"Hello, {name}.")

    with open("Save", "w") as fd:
        fd.write(name)
else:
    with open(save) as fd:
        name = fd.readline().rstrip()
    print(f'Nice to meet you again, {name}')
