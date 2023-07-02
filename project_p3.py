import mysql.connector as x

def ticket_booking():
    try:
        while True:
            c = int(input('Enter 1 to continue and 2 if you do not want to continue: '))
            if c == 1:
                db = x.connect(host='localhost', user='sqluser', password='password', database='rail')
                cur = db.cursor()
                name = input("Enter name: ")
                phone = int(input("Enter phone number: "))
                start = input("Enter starting point: ")
                end = input("Enter destination: ")
                date1 = input("Enter day (DD): ")
                date2 = input("Enter month (MM): ")
                date3 = input("Enter year (YYYY): ")
                time = input("Enter 1 to take the 3:00 PM train and 2 to take the 6:00 PM train: ")
                if time == '1':
                    t = '3:00PM'
                elif time == '2':
                    t = '6:00PM'
                else:
                    print('Invalid choice. Please enter information correctly.')
                    continue
                date = date1 + '/' + date2 + '/' + date3
                m = "count(*) from railway"
                w = cur.execute(m)
                u = w + 1
                s = "count(*) from railway where startpt='{}' and dest='{}' and date='{}' and time='{}'".format(start, end, date, t)
                l = cur.execute(s)
                if l == 200:
                    print('Train full. Please try booking for another train.')
                    continue
                elif l < 200:
                    q = "insert into railway values({}, {}, '{}', '{}', '{}', '{}', '{}')".format(u, phone, name, start, end, date, t)
                    cur.execute(q)
                    print('Your booking has been made successfully under unique ID', u, 'Please note and use for checking cancellation or updation.')
            elif c == 2:
                break
            else:
                print('Invalid choice. Please enter a number.')
                continue
            db.commit()
            cur.close()
            db.close()
    except:
        print("Error in code")
