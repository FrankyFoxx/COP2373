# Function to ask the user how many tickets they want to buy
def get_ticket_request():
    """
    Ask the user how many tickets they want to buy.
    Returns:
        int: number of tickets requested
    """
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
    if requested > 4:
        print("You cannot buy more than 4 tickets.")
        return 0

    if requested > remaining:
        print("Not enough tickets left for that purchase.")
        return 0

    return requested


# Main program logic wrapped in a function
def run_ticket_program():
    """
    Main logic for the cinema ticket pre-sale program.
    Handles looping, counting customers, and displaying results.
    """

    # Set the total number of tickets available
    total_tickets = 10

    # Accumulator to count how many customers successfully purchased tickets
    customer_count = 0

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

            # Increase the customer count since this was a successful purchase
            customer_count += 1

            # Inform the user of the updated ticket count
            print(f"Purchase successful! {total_tickets} tickets remaining.")
        else:
            # Inform the user that the purchase failed
            print("Purchase not completed. Try again.")

    # Once the loop ends, all tickets are sold
    print("\nAll tickets have been sold!")

    # Display the total number of customers
    print(f"Total number of customers: {customer_count}")


# Required structure for running the program
if __name__ == "__main__":
    run_ticket_program()
