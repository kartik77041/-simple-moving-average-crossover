import read
import mysql.connector
records = read.final


# # To create named HALNICO_database
# mydb = mysql.connector.connect(
# host='localhost',
# user='root',
# password='newrootpassword',
# )
# cur = mydb.cursor()
# cur.execute("create database HALNICO_database")

mydb = mysql.connector.connect(
host='localhost',
user='root',
password='newrootpassword',
database='db2'
)

# # COMMAND TO CREATE TABLE
# cur = mydb.cursor()
# s = "create table halnico(datetime DATETIME,close float, high float,low float,open float,volume INT,instrument VARCHAR(8))"
# cur.execute(s)
s = "insert into halnico(datetime ,close, high, low, open, volume, instrument) values(%s,%s,%s,%s,%s,%s,%s)"
cur = mydb.cursor()
cur.executemany(s,records)
mydb.commit()