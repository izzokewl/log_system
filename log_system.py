while True:
    try:
        nameinput = input("Enter full name: ").title().strip()
        if any(char.isdigit() for char in nameinput):
          raise ValueError("\nInvalid input, try again\n")
        break
    except ValueError as error:
       print(error)

