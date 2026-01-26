import inspect
import SheliaSportsman_Docstring_Exercise_1  # replace with your assignment name (without .py)

#replace docstring_example with your assignment name in the next 2 lines of code
with open("SheliaSportsman_Docstring_Exercise_1_design_doc.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {SheliaSportsman_Docstring_Exercise_1.__name__}\n\n")
    #replace with your name, the date, and the description of the program
    doc.write(f"# Name: Shelia Sportsman\n")
    doc.write(f"# Date: January 21, 2026\n")
    doc.write(f"# Program Description: Give brief description of your program\n\n")

    #replace docstring_example with your assignment name 
    for name, func in inspect.getmembers(SheliaSportsman_Docstring_Exercise_1, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")
    
    #replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/FrankyFoxx/COP2373.git")
print('Complete')