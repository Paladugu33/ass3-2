# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:32:47 2018

@author: hmohan
"""

import mysql.connector

# CONNECTING TO DATABASE
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
#connect to cursor                       
cursor = database.cursor()

# table creation
cursor.execute("CREATE TABLE pre_vio(name VARCHAR(255),address VARCHAR(255),zip_code VARCHAR(255),city VARCHAR(255),vio_code VARCHAR(255)) ")

#query for inner join
sql = """SELECT \
    INS1.facility_name as name, \
    INS1.facility_address as address, \
    INS1.facility_zip as zip_code, \
    INS1.facility_city as city, \
    VIO1.violation_code as vio_code \
    FROM VIO1\
    INNER JOIN INS1 ON INS1.serial_number=VIO1.serial_number"""
    
   

    
# insertion into table
  
cursor.execute(sql)
myresult = cursor.fetchall()

for i in range (0,len(myresult)):
    name = myresult[i][0]
    address = myresult[i][1]
    zip_code = myresult[i][2]
    city = myresult[i][3]
    vio_code = myresult[i][4]
    query = "INSERT INTO pre_vio (name,address,zip_code,city,vio_code) VALUES (%s,%s,%s,%s,%s)"
    values = (name,address,zip_code,city,vio_code)
    
    cursor.execute(query,values)
    database.commit()
print('Inserted into table pre_vio')
    
database.close()

