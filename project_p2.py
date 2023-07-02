from project_p3 import ticket_booking
from project_p4 import ticket_checking
from project_p5 import ticket_cancelling
from project_p6 import ticket_update

def menu():
    while True:
        print()
        print("1. Ticket Booking")
        print("2. Ticket Checking")
        print("3. Ticket Cancelling")
        print("4. Ticket Updating")
        print("5. Exit")
        c = int(input("Enter Choice: "))

        if c == 1:
            ticket_booking()
        elif c == 2:
            ticket_checking()
        elif c == 3:
            ticket_cancelling()
        elif c == 4:
            ticket_update()
        else:
            break
