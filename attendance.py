import json

def load_data():
    try:
        with open("attendance.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open("attendance.json", "w") as file:
        json.dump(data, file, indent=4)

def mark_attendance():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    status = input("Status (Present/Absent): ")

    data = load_data()
    data.append({
        "roll": roll,
        "name": name,
        "status": status
    })

    save_data(data)
    print("Attendance recorded!")

def view_attendance():
    data = load_data()
    if not data:
        print("No records found.")
        return

    for i, s in enumerate(data, 1):
        print(f"{i}. Roll: {s['roll']} | Name: {s['name']} | Status: {s['status']}")

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
