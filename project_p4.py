import mysql.connector as x

def ticket_checking():
    try:
        db = x.connect(host='localhost', user='sqluser', password='password', database='rail')
        cur = db.cursor()
        u = int(input('Please enter your booking unique ID to check your details: '))
        q = "select * from railway where uid='{}'".format(u)
        cur.execute(q)
        a = cur.fetchall()
        d = u - 1
        print('Your booking details are as follows:')
        print('Unique ID:', a[d][0])
        print('Phone Number:', a[d][1])
        print('Name:', a[d][2])
        print('Start Point:', a[d][3])
        print('Destination:', a[d][4])
        print('Date:', a[d][5])
        print('Time:', a[d][6])
        db.commit()
        cur.close()
        db.close()
    except:
        print("Unique ID not valid")
