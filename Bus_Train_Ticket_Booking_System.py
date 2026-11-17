
# Bus / Train Ticket Booking System
# Project PS No. 36

# Total seats and ticket price
total_seats = 10
ticket_price = 500

# List of available seats
available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dictionary to store passenger details
bookings = {}


# Function to display all seats
def view_seats():
    print("\n========== SEAT DETAILS ==========")

    for seat in range(1, total_seats + 1):

        if seat in bookings:
            print("Seat", seat, "- Booked")
        else:
            print("Seat", seat, "- Available")

    print("\nAvailable Seats:", len(available_seats))


# Function to book a ticket
def book_ticket():
    print("\n========== BOOK TICKET ==========")

    if len(available_seats) == 0:
        print("Sorry! All seats are booked.")
        return

    try:
        seat = int(input("Enter seat number (1-10): "))

        if seat < 1 or seat > total_seats:
            print("Invalid seat number.")

        elif seat not in available_seats:
            print("Sorry! This seat is already booked.")

        else:
            name = input("Enter passenger name: ").strip()

            if name == "":
                print("Passenger name cannot be empty.")
                return

            # Store passenger information
            bookings[seat] = {
                "name": name,
                "fare": ticket_price
            }

            # Remove booked seat from available seats
            available_seats.remove(seat)

            print("\nTicket booked successfully!")
            print("Passenger Name:", name)
            print("Seat Number:", seat)
            print("Ticket Price: Rs.", ticket_price)

            if len(available_seats) == 0:
                print("Bus is now full.")


    except ValueError:
        print("Please enter a valid number.")


# Function to display all bookings
def view_bookings():
    print("\n========== ALL BOOKINGS ==========")

    if len(bookings) == 0:
        print("No bookings available.")
        return

    for seat, passenger in bookings.items():

        print("\nPassenger Name:", passenger["name"])
        print("Seat Number:", seat)
        print("Ticket Price: Rs.", passenger["fare"])
        print("-----------------------------")


# Function to cancel a ticket
def cancel_booking():
    print("\n========== CANCEL TICKET ==========")

    try:
        seat = int(input("Enter seat number to cancel: "))

        if seat in bookings:

            passenger = bookings[seat]

            # Calculate 80 percent refund
            refund = passenger["fare"] * 80 // 100

            print("\nTicket cancelled successfully!")
            print("Passenger Name:", passenger["name"])
            print("Seat Number:", seat)
            print("Refund Amount: Rs.", refund)

            # Delete booking details
            del bookings[seat]

            # Make seat available again
            available_seats.append(seat)
            available_seats.sort()

        else:
            print("This seat is not booked.")

    except ValueError:
        print("Please enter a valid seat number.")


# Main program
while True:

    print("\n================================")
    print(" BUS / TRAIN TICKET BOOKING SYSTEM")
    print("================================")
    print("1. View Available Seats")
    print("2. Book Ticket")
    print("3. View All Bookings")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_seats()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        cancel_booking()

    elif choice == "5":
        print("\nThank you for using our Booking System!")
        print("Have a nice journey!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
