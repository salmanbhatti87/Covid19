# Movie Ticket Booking System
# Author: Python Programmer
# Version: 1.0

def initialize_movies():
    """Initialize and return the movies dictionary with available seats"""
    return {
        "Avengers": {"6PM": 20, "9PM": 15},
        "Inception": {"5PM": 10, "8PM": 8},
        "Interstellar": {"4PM": 12, "7PM": 10}
    }

def initialize_bookings():
    """Initialize and return an empty list for bookings"""
    return []

def display_welcome():
    """Display the welcome message"""
    print("\nWelcome to Movie Ticket Booking System")
    print("-------------------------------------")

def display_menu():
    """Display the main menu options"""
    print("\nMain Menu:")
    print("1. View Available Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Show Booking Summary")
    print("5. Exit")

def view_movies(movies):
    """Display available movies and showtimes"""
    print("\nAvailable Movies:")
    for movie, showtimes in movies.items():
        for showtime, seats in showtimes.items():
            print(f"{movie} ({showtime}): {seats} seats")

def book_ticket(movies, bookings):
    """Handle ticket booking process"""
    print("\nBook Ticket")
    view_movies(movies)
    
    movie = input("\nEnter movie name: ")
    if movie not in movies:
        print("Movie not found!")
        return
    
    showtime = input("Enter showtime: ")
    if showtime not in movies[movie]:
        print("Showtime not available for this movie!")
        return
    
    try:
        tickets = int(input("Enter number of tickets: "))
        if tickets <= 0:
            print("Please enter a positive number!")
            return
            
        if movies[movie][showtime] < tickets:
            print(f"Only {movies[movie][showtime]} seats available!")
            return
            
        # Update available seats
        movies[movie][showtime] -= tickets
        
        # Add to bookings
        bookings.append({
            "movie": movie,
            "showtime": showtime,
            "tickets": tickets
        })
        
        print(f"Booking confirmed for {movie} at {showtime} ({tickets} tickets)")
        
    except ValueError:
        print("Please enter a valid number!")

def cancel_ticket(movies, bookings):
    """Handle ticket cancellation process"""
    if not bookings:
        print("\nNo bookings found to cancel!")
        return
    
    print("\nYour Bookings:")
    for i, booking in enumerate(bookings, 1):
        print(f"{i}. {booking['movie']} | {booking['showtime']} | {booking['tickets']} tickets")
    
    try:
        choice = int(input("\nEnter booking number to cancel: ")) - 1
        if 0 <= choice < len(bookings):
            booking = bookings.pop(choice)
            movies[booking["movie"]][booking["showtime"]] += booking["tickets"]
            print(f"Cancelled {booking['tickets']} tickets for {booking['movie']} at {booking['showtime']}")
        else:
            print("Invalid booking number!")
    except ValueError:
        print("Please enter a valid number!")

def show_summary(bookings):
    """Display booking summary"""
    if not bookings:
        print("\nNo bookings yet!")
        return
    
    print("\nBooking Summary:")
    for booking in bookings:
        print(f"- {booking['movie']} | {booking['showtime']} | {booking['tickets']} tickets")

def main():
    """Main function to run the booking system"""
    movies = initialize_movies()
    bookings = initialize_bookings()
    display_welcome()
    
    while True:
        display_menu()
        
        try:
            option = int(input("\nChoose option (1-5): "))
            
            if option == 1:
                view_movies(movies)
            elif option == 2:
                book_ticket(movies, bookings)
            elif option == 3:
                cancel_ticket(movies, bookings)
            elif option == 4:
                show_summary(bookings)
            elif option == 5:
                print("\nThank you for using our Movie Ticket Booking System. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-5.")
                
        except ValueError:
            print("Please enter a valid number (1-5)!")

if __name__ == "__main__":
    main()