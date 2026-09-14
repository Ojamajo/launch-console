name = input("What's your name? ")

print("Welcome to " + name + "'s Launch Console!")

running = True

while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")

    choice = input("Pick 1-3: ")

    if choice == "1":
        print("I'm interested in computer science and technology.")

    elif choice == "2":
        print("My goal is to improve my coding skills and build real projects.")

    elif choice == "3":
        print("Goodbye!")
        running = False

    else:
        print("Please pick 1, 2, or 3.")