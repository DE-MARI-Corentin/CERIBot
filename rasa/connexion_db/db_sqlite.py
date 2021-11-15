import sqlite3

def init_data():
 conn = sqlite3.connect('demo.db') 
 cursor = conn.cursor()
 print("Database created and Successfully Connected to SQLite")
 
 sql='''CREATE TABLE d2(
    section VARCHAR,
    grp VARCHAR,
    name VARCHAR,
    room VARCHAR,
    time VARCHAR
  )'''
 cursor.execute(sql)
 
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","alternant","math","S2","11:00"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","alternant","infra","S3","13:00"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","classique","math","S2","11:00"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","classique","web","S8","13:00"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","alternant","IA","S5","11:00"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","alternant","ingedoc","S7","13:00"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","classique","anglais","S4","11:30"))
 cursor.execute('''INSERT INTO d2(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","classique","ecom","S6","13:30"))

 print("Table created successfully........")

 # Commit your changes in the database
 conn.commit()

 #Closing the connection
 conn.close()

def select_data(section,group):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('''SELECT * FROM d2 WHERE section=? AND grp=?''',(section,group,))
  
  rows = cursor.fetchall()

  text =""
  for row in rows:
    print(row)
    text = row[2]+" in "+row[3]+" at "+row[4]
    break

  #Closing the connection
  conn.close()
  
  return text;

def print_data():
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('''SELECT * FROM d2''',)
  
  rows = cursor.fetchall()

  for row in rows:
    print(row)

  #Closing the connection
  conn.close()

if __name__ == "__main__":
 init_data()
 print("All data:")
 print_data()
 print("Select classique")
 print(select_data("","classique"))
 
