filename = "guest_book.txt"
with open(filename, 'w') as file_object:
    count = 0
    while True:
        name = input("Enter your name: \n")
        if name == 'quit':
            break
        file_object.write(name)
        writee = f"\nHello {name}\n"
        print(writee)
        file_object.write(writee)
        count += 1
