# Railway-Reservation-System

The Railway Reservation System is a Python-based application that provides users with the ability to perform various tasks related to ticket booking, checking, canceling, and updating. The project utilizes a MySQL database to store user login information and is built using a Python and MySQL interface.

Users can perform the following tasks:

1. Ticket Booking: Users can book train tickets by providing their name, phone number, starting point, destination, date, and preferred train timing (3:00 PM or 6:00 PM). The system checks for seat availability and assigns a unique ID to each booking. If the selected train is full, users are prompted to choose another train.

2. Ticket Checking: Users can check their booking details by entering their unique booking ID. The system retrieves the corresponding details from the MySQL database, including the name, phone number, starting point, destination, date, and timing of the booked train.

3. Ticket Cancelling: Users can cancel their booked tickets by providing their booking ID. The system removes the booking entry from the MySQL database and displays a confirmation message indicating the successful cancellation of the ticket.

4. Ticket Updating: Users can update their booking details, such as the name or timing of the train, by entering their booking ID and selecting the desired update option. The system updates the corresponding entry in the MySQL database and provides a confirmation message.

The project emphasizes the use of a Python and MySQL interface to connect the application with the database. The MySQL database stores the necessary information for ticket bookings and allows for efficient retrieval and modification of data.

Overall, the Railway Reservation System provides users with a convenient and user-friendly interface to manage their train ticket bookings. It ensures accurate seat availability, secure storage of user information, and seamless interaction between the Python application and the MySQL database.
