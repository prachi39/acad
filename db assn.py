#1

import sqlite3
conn=sqlite3.connect('test3.db')
print("opened database successfuly")


#conn.execute('''CREATE TABLE BOOK
         #(BOOK_ID    INT       NOT NULL,
            # TITLE_ID   INT        NOT NULL,
            # LOCATION  CHAR(50),
             #GENRE   REAL)''')
#print("Table created successfully")



#conn.execute('''CREATE TABLE TITLES
            # (TITLE_ID    INT       NOT NULL,
             #TITLE        TEXT      NOT NULL,
             #ISBN        CHAR(50),
             #PUBLISHER_ID  INT      NOT NULL,
             #PUBLICATION_YEAR  REAL)''')
#print("Table created successfully")


#conn.execute('''CREATE TABLE PUBLISHERS
            #(PUBLISHER_ID    INT  PRIMARY KEY     NOT NULL,
             #NAME      TEXT      NOT NULL,
             #STREET_ADDRESS       CHAR(50),
             #SUITE_NUMBER  INT      NOT NULL,
             #ZIPCODE_ID  REAL)''')
#print("Table created successfully")


#conn.execute('''CREATE TABLE ZIPCODES
           # (ZIPCODE_ID    INT  PRIMARY KEY     NOT NULL,
            # CITY          TEXT      NOT NULL,
             #STATE         CHAR(50),
             #ZIPCODE       REAL)''')
#print("Table created successfully")


#conn.execute('''CREATE TABLE AUTHOR_TITLES
            #(AUTHOR_TITLE_ID    INT  PRIMARY KEY     NOT NULL,
             #AUTHOR_ID          INT    NOT NULL,
             #TITLE_ID          REAL)''')
#print("Table created successfully")

#conn.execute('''CREATE TABLE AUTHORS
            #(AUTHOR_ID    INT  PRIMARY KEY     NOT NULL,
            # FIRST_NAME   TEXT   NOT NULL,
             #MIDDLE_NAME  TEXT   NOT NULL,
             # LAST_NAME    REAL)''')
#print("Table created successfully")

#2

#conn.execute("INSERT INTO BOOK(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(11,56,'DS','ss')")
#conn.execute("INSERT INTO BOOK(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(22,33,'EE','so')")
#conn.commit()
#print("records created successfully")
#conn.close()

#conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,PUBLISHER_ID,PUBLICATION_YEAR)VALUES(4,'DS',5,2015)")
#conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,PUBLISHER_ID,PUBLICATION_YEAR)VALUES(5,'EE',7,2005)")
#conn.commit()
#print("records created successfully")
#conn.close()

#conn.execute("INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER)VALUES(4,'AAA',412,30)")
#conn.execute("INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER)VALUES(5,'PPP',899,13)")
#conn.commit()
#print("records created successfully")
#conn.close()

#conn.execute("INSERT INTO ZIPCODES(ZIPCODE_ID,CITY)VALUES(12,'APA')")
#conn.execute("INSERT INTO ZIPCODES(ZIPCODE_ID,CITY)VALUES(13,'DFD')")
#conn.commit()
#print("records created successfully")
#conn.close()

#conn.execute("INSERT INTO AUTHOR_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID)VALUES(12,19)")
#conn.execute("INSERT INTO AUTHOR_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID)VALUES(13,20)")
#conn.commit()
#print("records created successfully")
#conn.close()

#conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME)VALUES(3,'A','P','A')")
#conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME)VALUES(1,'P','A','P')")
#conn.commit()
#print("records created successfully")
#conn.close()

#3

cursor=conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOK ")
for row in cursor:
 print("BOOK_ID=",row[0])
 print("TITLE_ID=",row[1])
 print("LOCATION=",row[2])
 print("GENRE=",row[3],"\n")
print("operation done successfully")

conn.execute("UPDATE BOOK set TITLE_ID=44 where BOOK_ID=11")
conn.commit()
print("Total number of rows updated:",conn.total_changes)
print("the original value is 56")
print("the updated value is 44 ")