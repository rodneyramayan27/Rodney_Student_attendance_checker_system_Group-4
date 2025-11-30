import csv
import os
from datetime import datetime

# =========================
# Student Attendance Checker
# Subject: ITE 366
# =========================

FILENAME = "ITE366_Attendance.csv"

def load_data():
    """Load existing attendance data from CSV file"""
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    else:
        data.append(["Date", "Student Name", "Status"])
    return data


def save_data(data):
    """Save attendance data to CSV file"""
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def view_attendance(data):
    """Display all attendance records"""
    print("\n=====  ATTENDANCE RECORD =====")
    if len(data) <= 1:
        print("No attendance data found yet.\n")
        return

    header = data[0]
    records = data[1:]

    print(f"{header[0]:<12} | {header[1]:<20} | {header[2]}")
    print("-" * 38) 

    for row in records:
        print(f"{row[0]:<12} | {row[1]:<20} | {row[2]}")
    print()


def mark_attendance(data):
    """Mark attendance for students with improved looping prompt."""
    date_today = datetime.now().strftime("%Y-%m-%d")
    print(f"\nMarking attendance for {date_today}")
    print("Enter student names one by one.")
    print("------------------------------")

    while True:
        student = input("Student Name: ").strip().title()

        if not student:
            print(" Student name cannot be empty. Try again.")
            continue

        status = input(f"Is {student} Present (P) or Absent (A)? ").strip().upper()
        if status not in ["P", "A"]:
            print(" Invalid input. Please enter 'P' or 'A'.")
            continue

        data.append([date_today, student, "Present" if status == "P" else "Absent"])
        print(f" -> Attendance recorded for {student}.\n")


        done_check = input("If you're done type Done : ").strip().lower()
        print() 
        if done_check == "done":
            break

    save_data(data)
    print("Saved\n")


def main():
    """Main program menu"""
    data = load_data()

    while True:
        print("====================================")
        print("  STUDENT ATTENDANCE CHECKER - ITE 366")
        print("====================================")
        print("1. Mark Attendance")
        print("2. View Attendance Record")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            mark_attendance(data)
        elif choice == "2":
            view_attendance(data)
        elif choice == "3":
            print("\n Goodbye! Attendance data has been saved.")
            save_data(data)
            break
        else:
            print(" Invalid choice. Please try again.\n")


if __name__ == "_main_":
    main()