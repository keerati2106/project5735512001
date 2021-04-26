import pymysql


serial_no = input("RFID card U_ID ?")
user_id = input("user name?")


serial_no = serial_no.upper()



sql_con = pymysql.connect(host='localhost', user='root',
                          passwd='test1234', db='gate_inspection')
sqlcursor = sql_con.cursor()




sql_request = 'SELECT card_id,serial_no,user_id,valid' + \
              ' FROM cards  WHERE serial_no = "' + serial_no + '"'

count = sqlcursor.execute(sql_request)

if count > 0:
    print("Error! RFID card {} already in database".format(serial_no))
    T = sqlcursor.fetchone()
    print(T)
else:
    sql_insert = 'INSERT INTO cards (serial_no,user_id,valid) ' + \
                 'values("{}","{}","1")'.format(serial_no, user_id)
    count = sqlcursor.execute(sql_insert)
    if count > 0:
        sql_con.commit()
        
        count = sqlcursor.execute(sql_request)
        if count > 0:
            print("RFID card {} inserted to database".format(serial_no))
            T = sqlcursor.fetchone()
            print(T)
    if count == 0:
        print("Error! RFID card {} not inserted to database! ".format(
               serial_no))

