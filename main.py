import random

class myParkingGarage():

    def __init__(self):
        self.available_tickets = list(range(1, 21))
        self.available_spots = list(range(1, 21))
        self.current_ticket = {}
        
    def takeTicket(self):
            if self.available_tickets:
                ticket = random.choice(self.available_tickets)
                self.available_tickets.remove(ticket)
                spot = random.choice(self.available_spots)
                self.available_spots.remove(spot)
                self.current_ticket[ticket] = {'spot': spot, 'paid': False}
                print(f"Welcome to Shirley's Garage! Here is your ticket. Ticket number {ticket}")
            else:
                print("Sorry, the garage is full.")
                
    def payForParking(self):
            ticket = int(input("Please enter your ticket number: "))
            if ticket in self.current_ticket and not self.current_ticket[ticket]['paid']:
                payment = input("Please enter your payment amount: ")
                if payment:
                    self.current_ticket[ticket]['paid'] = True
                    print("Thank you for your payment. You have 15 minutes to leave the garage.")
                else:
                    print("Payment not received.")
            else:
                print("Invalid ticket number or ticket already paid.")
                
    def leaveGarage(self):
            ticket = int(input("Please enter your ticket number: "))
            if ticket in self.current_ticket and self.current_ticket[ticket]['paid']:
                spot = self.current_ticket[ticket]['spot']
                self.available_tickets.append(ticket)
                self.available_spots.append(spot)
            elif self.current_ticket[ticket]:
                print("Thank you for visiting Shirley's Garage. Have a nice day!")
            elif ticket in self.current_ticket and not self.current_ticket[ticket]['paid']:
                payment = input("Your ticket has not been paid. Please enter your payment amount: ")
                if payment:
                    self.current_ticket[ticket]['paid'] = True
                    spot = self.current_ticket[ticket]['spot']
                    self.available_tickets.append(ticket)
                    self.available_spots.append(spot)
                    print("Thank you for your payment. You have 15 minutes to leave the garage.")
                    print("Thank you for visiting Shirley's Garage. Have a nice day!")
                else:
                    print("Payment not received.")
            else:
                print("Invalid ticket number.")
# Main program loop
my_garage = myParkingGarage()
while True:
    print("Welcome to Shirley's Garage!")
    print("1. Take Ticket")
    print("2. Pay for Parking")
    print("3. Leave Garage")
    print("4. Exit")
    choice = input("Please choose an option: ")
    if choice == "1":
        my_garage.takeTicket()
    elif choice == "2":
        my_garage.payForParking()
    elif choice == "3":
        my_garage.leaveGarage()
    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.")