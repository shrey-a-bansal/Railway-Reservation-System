import mysql.connector as x

def ticket_update():
    try:
        db = x.connect(host='localhost', user='sqluser', password='password', database='rail')
        cur = db.cursor()
        while True:
            n = int(input('1. Change name\n2. Change timing\n'))
            if n == 1:
                u = int(input('Enter booking unique ID: '))
                n1 = input('Enter updated name: ')
                q = "update railway set name='{}' where uid='{}'".format(n1, u)
                print('Name successfully updated to:', n1)
            elif n == 2:
                u = int(input('Enter booking unique ID: '))
                t = int(input('Enter 1 for changing time to 3:00 PM and 2 for changing time to 6:00 PM: '))
                if t == 1:
                    t1 = '3:00PM'
                    q = "update railway set time='{}' where uid='{}'".format(t1, u)
                elif t == 2:
                    t1 = '6:00PM'
                    q = "update railway set time='{}' where uid='{}'".format(t1, u)
                else:
                    print('Invalid entry. Try again.')
                    continue
            else:
                break
        db.commit()
        cur.close()
        db.close()
    except:
        print("Error in code")
