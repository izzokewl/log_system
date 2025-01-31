import datetime

attendance = {}

print("\n=======LOG ATTENDANCE=======\n")
while True:
    try:
        nameinput = input("Enter full name: ").title().strip()
        if any(char.isdigit() for char in nameinput):
            raise ValueError("\nInvalid input, try again\n")
        break
    except ValueError as error:
        print(error)

if nameinput not in attendance:
    attendance[nameinput] = {}

log_entries = ["Log in", "Out for lunch", "Back from lunch", "Log out"]
attempt = len(attendance[nameinput])

if attempt < len(log_entries):
    log_time = datetime.datetime.now().strftime("%H:%M")

    attendance[nameinput][log_entries[attempt]] = log_time
    
    print(f"{nameinput} punched for {log_entries[attempt]}")
    print(f"Time punched: {log_time}\n")
else:
    print(f"{nameinput} has already completed punches for the day\n")