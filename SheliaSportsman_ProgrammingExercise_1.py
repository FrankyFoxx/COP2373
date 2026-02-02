# Function to ask the user how many tickets they want
def get_ticket_request():
    """
    Ask the user how many tickets they want to buy.

    Returns:
        int: number of tickets requested
    """
    # Prompt the user for how many tickets they want and return the number
    return int(input("How many seats would you like to reserve (max 4)? "))


# Function to validate and process the sale
def process_sale(requested, remaining):
    """
    Validate the ticket request and determine how many tickets can be sold.

    Args:
        requested (int): tickets the user wants
        remaining (int): tickets still available

    Returns:
        int: number of tickets sold (0 if invalid)
    """
    # Check if the user is trying to buy more than the allowed limit
    if requested > 4:
        print("You cannot buy more than 4 tickets.")
        return 0

    # Check if the user is trying to buy more tickets than remain
    if requested > remaining:
        print("Not enough tickets left for that purchase.")
        return 0

    # If the request is valid, return the number requested
    return requested


# Main program logic wrapped in a function
def run_ticket_program():
    """
    Main logic for the cinema ticket pre-sale program.
    Handles looping, counting buyers, and displaying results.
    """

    # Set the total number of tickets available
    total_tickets = 10

    # Accumulator to count how many buyers successfully purchased tickets
    buyers = 0

    # Display a welcome message to the user
    print("Welcome to the Cinema Ticket Pre-Sale!")

    # Loop continues until all tickets are sold
    while total_tickets > 0:

        # Show the user how many tickets are still available
        print(f"\nTickets remaining: {total_tickets}")

        # Ask the user how many tickets they want
        request = get_ticket_request()

        # Validate the request and determine how many tickets can be sold
        sold = process_sale(request, total_tickets)

        # If the sale is valid, update totals
        if sold > 0:
            # Subtract the sold tickets from the total
            total_tickets -= sold

            # Increase the buyer count since this was a successful purchase
            buyers += 1

            # Inform the user of the updated ticket count
            print(f"Purchase successful! {total_tickets} tickets remaining.")
        else:
            # Inform the user that the purchase failed
            print("Purchase not completed. Try again.")

    # Once the loop ends, all tickets are sold
    print("\nAll tickets have been sold!")

    # Display the total number of buyers
    print(f"Total number of buyers: {buyers}")


# Required structure for running the program
if __name__ == "__main__":
    # Call the main program function to start the ticket sale process
    run_ticket_program()
