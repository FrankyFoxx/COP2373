from functools import reduce

def get_expenses():
    expenses = []

    print("Enter your monthly expenses.")
    print("Type 'done' when finished.\n")

    while True:
        expense_type = input("Enter the type of expense (or 'done'): ").strip()

        if expense_type.lower() == "done":
            break

        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.\n")

    return expenses


def main():
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    # Total using reduce
    total_expense = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # Highest expense using reduce
    highest_expense = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Lowest expense using reduce
    lowest_expense = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    print("\n----- Expense Summary -----")
    print(f"Total Monthly Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} — ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} — ${lowest_expense[1]:.2f}")


if __name__ == "__main__":
    main()