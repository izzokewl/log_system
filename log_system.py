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

def attendance_list():
    print("\n=======ATTENDANCE LIST=======\n")
    for name, logs in attendance.items():
        print(f"{name}:")
        for entry, time in logs.items():
            print(f"  {entry}: {time}")
    print("\n=============================\n")

print("\n=======LOG ATTENDANCE=======\n")
while True:
    nameinput = input("Enter full name: ").title().strip()
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
            view_list = input("Do you want to see the attendance list? (type 'list' to view or 'no' to continue logging)\n").strip().upper()
            if view_list == "LIST":
                attendance_list()
            break 
        elif new_entry == "NO":
            print("Thank you for logging attendance")
            exit() 
        else:
            print("\nYou have entered a wrong input, please enter YES or NO\n")
