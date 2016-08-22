'''
Created on 20 ago. 2016

@author: Ivan Villar
'''
#!/usr/bin/python

import MySQLdb as mdb

def connectadatabase():
    global con
    con = mdb.connect('localhost', 'root', '', 'dondeesta');
    return con

def insert(table, fields, values, filters):  
    cur = con.cursor()
    cur.execute("INSERT INTO"+ table +"("+fields+") VALUES("+values+")")
    con.commit()
    
def update(table, fields, values, filters):
    #UPDATE t1 SET col1 = col1 + 1, col2 = col1;
    valuesArray = values.split(',')
    fieldsArray = fields.split(',')
    
    counter = 0
    for val in fieldsArray:
        if counter == 0:
            newValues = "SET "+ val +" = '"+valuesArray[counter]+"'"
        else:
            newValues = newValues + " , "+ val + "='" + valuesArray[counter] + "'"
        counter = counter + 1
        
    cur = con.cursor()
    cur.execute("UPDATE " + table + " "+ newValues +" WHERE "+ filters)
    con.commit()    

def select(table, fields, filters):
    cur = con.cursor()
    cur.execute("SELECT " + fields + " FROM "+ table +" WHERE "+ filters)
    con.commit()
    results = cur.fetchone() #Basically this save the results in an array
    
    return results

def delete(table, fields, values):
    valuesArray = values.split(',')
    fieldsArray = fields.split(',')
    
    counter = 0
    for val in fieldsArray:
        if counter == 0:
            filter = "WHERE "+ val +" = '"+valuesArray[counter]+"'"
        else:
            filter = filter + " AND "+ val + "='" + valuesArray[counter] + "'"
        counter = counter + 1
    
    cur = con.cursor()
    cur.execute("DELETE FROM "+ table +" "+ filter)
    con.commit()

connectadatabase()  #First things first
update("direcciones","nombre,direccion","periquitazo,periquito calle jaja","ref=2")
