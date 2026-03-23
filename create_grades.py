import csv

def create_grades_file():
    # Ask how many students to enter
    num_students = int(input("How many students do you want to enter? "))

    # Open CSV file for writing
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop for each student
        for i in range(num_students):
            print(f"\nEntering data for student {i+1}:")
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the row to the CSV
            writer.writerow([first, last, exam1, exam2, exam3])

    print("\ngrades.csv has been created successfully.")


if __name__ == "__main__":
    create_grades_file()