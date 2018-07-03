import sqlite3
conn=sqlite3.connect('test.db')
print("opened database successfuly")


#conn.execute('''CREATE TABLE COMPANY
            # (ID INT PRIMARY KEY  NOT NULL,
            # NAME      TEXT       NOT NULL,
            # AGE       INT        NOT NULL,
            # ADDRESS   CHAR(50),
            # SALARY    REAL)''')
#print("Table created successfully")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(7,'PPP',32,'FGDF',20000)")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(4,'PRP',31,'FGTF',10000)")
#conn.commit()
#print("records created successfully")
cursor=conn.execute("SELECT ID,NAME,ADDRESS,AGE from COMPANY ")
for row in cursor:
 print("ID=",row[0])
 print("NAME=",row[1])
 print("ADDRESS=",row[2])
 print("AGE=",row[3],"\n")
#print("operation done successfully")

#conn.execute("UPDATE COMPANY set AGE=18 where ID=1")
#conn.commit()
#print("total no of rows updated:",conn.total_changes)
conn.execute("DELETE from COMPANY where ID=1")
conn.commit()
print("operation done successfully")
conn.close()
