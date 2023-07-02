import mysql.connector as x

def ticket_cancelling():
    try:
        db = x.connect(host='localhost', user='sqluser', password='password', database='rail')
        cur = db.cursor()
        u = int(input("Enter your booking unique ID: "))
        q = "delete from railway where uid='{}'".format(u)
        r = cur.execute(q)
        rr = cur.fetchall()
        d = u - 1
        print('Ticket under unique ID', u, 'booked by', rr[d][2], 'from', rr[d][3], 'to', rr[d][4], 'on', rr[d][5], 'at', rr[d][6], 'cancelled successfully')
        db.commit()
        cur.close()
        db.close()
    except:
        print("Unique ID not valid")
