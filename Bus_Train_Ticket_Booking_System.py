
# Bus / Train Ticket Booking System
# Project PS No. 36

total_seats = 10
ticket_price = 500

# Store available seats in a list
available_seats = list(range(1, total_seats + 1))

# Store passenger details in a dictionary
bookings = {}


# Function 1: View Available Seats
def view_seats():
    if available_seats:
        print("Available:", ", ".join(map(str, available_seats)))
    else:
        print("No seats available. Bus is full.")


# Function 2: Book a Seat
def book_seat():
    try:
        seat = int(input("Seat: "))
    except ValueError:
        print("Invalid seat. Choose a seat from 1 to 10.")
        return

    if seat < 1 or seat > 10:
        print("Invalid seat. Choose a seat from 1 to 10.")
        return

    if seat not in available_seats:
        print(f"Seat {seat} is already booked.")
        return

    passenger = input("Passenger: ").strip()

    if not passenger:
        print("Invalid passenger name.")
        return

    bookings[seat] = passenger
    available_seats.remove(seat)

    print(f"Seat {seat} booked for {passenger}. Fare: {ticket_price}")
    print(f"Seats left: {len(available_seats)}")

    if len(available_seats) == 0:
        print("Bus is now full.")


# Function 3: View All Bookings
def view_bookings():
    if bookings:
        print("Booking Details:")
        for seat, passenger in sorted(bookings.items()):
            print(f"Seat {seat}: {passenger}")
    else:
        print("No bookings found.")


# Function 4: Cancel a Booking
def cancel_booking():
    try:
        seat = int(input("Seat: "))
    except ValueError:
        print("Invalid seat number.")
        return

    if seat not in bookings:
        print("No booking found for this seat.")
        return

    passenger = bookings.pop(seat)
    refund = int(ticket_price * 0.80)

    available_seats.append(seat)
    available_seats.sort()

    print(f"Booking for seat {seat} cancelled. Refund: {refund}")


# Main Menu
while True:
    print("\n===== BUS / TRAIN TICKET BOOKING SYSTEM =====")
    print("1. View seats")
    print("2. Book")
    print("3. Bookings")
    print("4. Cancel")
    print("5. Exit")

    try:
        choice = int(input("Enter menu option: "))
    except ValueError:
        print("Invalid menu option. Try again.")
        continue

    if choice == 1:
        view_seats()

    elif choice == 2:
        book_seat()

    elif choice == 3:
        view_bookings()

    elif choice == 4:
        cancel_booking()

    elif choice == 5:
        print("Thank you for using the booking system!")
        break

    else:
        print("Invalid menu option. Choose 1 to 5.")
