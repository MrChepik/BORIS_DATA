#!/usr/bin/env python3
#-*-decode='utf-8'-*-

import ibm_db
import pandas as pd
import ibm_db_dbi

#Replace the placeholder values with your actual Db2 hostname, username, and password:
dsn_hostname = "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "gqw76927"        # e.g. "abc12345"
dsn_pwd = "2t^lrpsgv2dphfvx"      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"


#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)

#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
#Create database connection

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )
    
createQuery = 'create table INSTRUCTOR (ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR (30), LNAME VARCHAR (30), CITY VARCHAR (10), CCODE CHARACTER (2))'
createStmt = ibm_db.exec_immediate(conn, createQuery)

insertQuery = 'insert into INSTRUCTOR VALUES(1, 'First_Name', 'Last_Name', 'CITY', 'CC')'
insertStmt = ibm_db.exec_immediate(conn, insertQuery)

insertQuery_2 = 'insert into INSTRUCTOR VALUES(2, 'First_Name2', 'Last_Name2', 'CITY2', 'CC')'
insertStmt = ibm_db.exec_immediate(conn, insertQuery_2)

insertQuery_3 = 'insert into INSTRUCTOR VALUES(3, 'First_Name3', 'Last_Name3', 'CITY3', 'CC')'
insertStmt = ibm_db.exec_immediate(conn, insertQuery_3)

selectQuery = 'select * from INSTRUCTOR'
selectStmt = ibm_db.exec_immediate(conn, selectQuery)
fetchStmt = ibm_db.fetch_both(selectStmt)

updateQery = "update INSTRUCTOR set CITY = CITY5 where FNAME = 'Firstname'"
updateStmt = ibm_db.exec_immediate(conn, updateQuery)

pconn = ibm_db_dbi.connection(conn)

selectQuery = select * from Instructor

pdf = pd.read_sql(selectQuery, pconn)

pdf.head()


