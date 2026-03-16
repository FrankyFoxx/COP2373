import inspect
import SheliaSportsman_Prog_Exercise07  # your assignment module (no .py)

# Open the output document
with open("SheliaSportsman_Prog_Exercise07.txt", "w") as doc:
    # Header information
    doc.write("# Technical Design Document: SheliaSportsman_Prog_Exercise07n\n")
    doc.write("Name: Shelia Sportsman\n")
    doc.write("Date: March 016, 2026\n")
    doc.write("Program Description: Give brief description of your program\n\n")

    # Loop through functions in the module
    for name, func in inspect.getmembers(SheliaSportsman_Prog_Exercise07, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    # Repository link
    doc.write("Link to your repository: https://github.com/FrankyFoxx/COP2373.git")

print("Complete")