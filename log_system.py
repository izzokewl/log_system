import datetime

attendance = {}

def log_attendance(nameinput):
    if nameinput not in attendance:
        attendance[nameinput] = {}

def punch_entry(nameinput, log_entries, attempt):
    if attempt < len(log_entries):
        log_time = datetime.datetime.now().strftime("%H:%M")
        attendance[nameinput][log_entries[attempt]] = log_time
        print(f"{nameinput} punched for {log_entries[attempt]}")
        print(f"Time punched: {log_time}\n")
    else:
        print(f"{nameinput} has already completed punches for the day\n")

print("\n=======LOG ATTENDANCE=======\n")
while True:
    nameinput = input("\nEnter full name: ").title().strip()
    if any(char.isdigit() for char in nameinput):
        print("\nInvalid input, try again\n")
        continue

    log_attendance(nameinput)
    log_entries = ["Log in", "Out for lunch", "Back from lunch", "Log out"]
    attempt = len(attendance[nameinput])
    punch_entry(nameinput, log_entries, attempt)


    while True:
        new_entry = input("Do you want to punch another entry?\nYES or NO\n").strip().upper()
        if new_entry == "YES":
            break
        elif new_entry == "NO":
            print("Thank you for logging attendance.")
        else:
            print("\nYou have entered a wrong input, please enter YES or NO\n")
