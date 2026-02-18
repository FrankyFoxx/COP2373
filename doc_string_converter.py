import inspect
import SheliaSportsman_ProgrammingExercise_3  # your assignment module (no .py)

# Open the output document
with open("SheliaSportsman_ProgrammingExercise_3.txt", "w") as doc:
    # Header information
    doc.write("# Technical Design Document: SheliaSportsman_ProgrammingExercise_3\n\n")
    doc.write("Name: Shelia Sportsman\n")
    doc.write("Date: February 17, 2026\n")
    doc.write("Program Description: Give brief description of your program\n\n")

    # Loop through functions in the module
    for name, func in inspect.getmembers(SheliaSportsman_ProgrammingExercise_3, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    # Repository link
    doc.write("Link to your repository: https://github.com/FrankyFoxx/COP2373.git")

print("Complete")