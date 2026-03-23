import csv

def display_grades():
    print("\nStudent Grades:\n")
    print(f"{'First Name':<12}{'Last Name':<12}{'Exam 1':<8}{'Exam 2':<8}{'Exam 3':<8}")
    print("-" * 50)

    # Read the CSV file
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            first, last, e1, e2, e3 = row
            print(f"{first:<12}{last:<12}{e1:<8}{e2:<8}{e3:<8}")


if __name__ == "__main__":
    display_grades()