import numpy 
import pylab
import MySQLdb
import sys 

database = MySQLdb.connect(host="localhost",user="root",passwd="1",db="SensorInformation")

cursor = database.cursor()

database.query("select * from pHOutput")

buffer = database.store_result()
output = buffer.fetch_row(0)
cursor.close()
database.close()
print output

