'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. 
'''
class Train:

    def book_ticket(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully.")
        else:
            print("Not enough seats available.")
    def get_status(self):
        print(f"Available seats: {self.available_seats}")
    def get_fare_info(self):
        print(f"Fare per ticket: {self.fare_per_ticket} INR")
    def __init__(self, train_name, available_seats, fare_per_ticket):
        self.train_name = train_name
        self.available_seats = available_seats
        self.fare_per_ticket = fare_per_ticket
        print(f"Train {self.train_name} initialized with {self.available_seats} seats and fare {self.fare_per_ticket} INR.")
# Example usage
train = Train("Rajdhani Express", 100, 1500)
train.get_status()  # Output: Available seats: 100
train.get_fare_info()  # Output: Fare per ticket: 1500 INR
train.book_ticket(5)  # Output: 5 tickets booked successfully.
train.get_status()  # Output: Available seats: 95
train.get_fare_info()  # Output: Fare per ticket: 1500 INR
train.book_ticket(200)  # Output: Not enough seats available.
train.get_status()  # Output: Available seats: 95
train.get_fare_info()  # Output: Fare per ticket: 1500 INR
# Output: Train Rajdhani Express initialized with 100 seats and fare 1500 INR.
