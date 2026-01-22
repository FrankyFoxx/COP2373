def get_ticket_request():
    """
    Ask the user how many tickets they want to buy.

    Returns:
        int: The number of tickets requested by the user.
    """
    return int(input("How many tickets would you like to buy (max 4)? "))


def process_sale(requested, remaining):
    """
    Validate a ticket purchase request and determine how many tickets can be sold.

    Args:
        requested (int): Number of tickets the user wants to buy.
        remaining (int): Number of tickets still available.

    Returns:
        int: The number of tickets sold. Returns 0 if the request is invalid.
    """
    if requested > 4:
        print("You cannot buy more than 4 tickets.")
        return 0
    if requested > remaining:
        print("Not enough tickets left for that purchase.")
        return 0
    return requested


# MAIN PROGRAM
total_tickets = 20
buyers = 0

print("Welcome to the Cinema Ticket Pre-Sale!")

while total_tickets > 0:
    print(f"\nTickets remaining: {total_tickets}")

    request = get_ticket_request()
    sold = process_sale(request, total_tickets)

    if sold > 0:
        total_tickets -= sold
        buyers += 1
        print(f"Purchase successful! {total_tickets} tickets remaining.")
    else:
        print("Purchase not completed. Try again.")

print("\nAll tickets have been sold!")
print(f"Total number of buyers: {buyers}")