from sqlite3 import *
#question no.1
print("<--------solution 1-------->")
try:
    con = connect('Students.db')
    print("Database created")
#question no.2
    print("<--------solution 2-------->")    
    l=[]
    for i in range(1,11):
        name=input("Enter your name")
        while(1):
            marks=int(input("Enter your marks"))
            if 0<=marks<=100:
                break;
            else:
                print("Please enter your marks between the range(0-100)")
        my=(name,marks)
        l.append(my)
#question no.3
    print("<--------solution 3-------->")
    print()
    cur=con.cursor()
    query='create table students(Name varchar(50),Marks double(3,1));'
    cur.execute(query)
    print("table created")
    print()
    query = 'Insert into students(Name,Marks) values (?,?);'
    cur.executemany(query,l)
    query = 'select Name from students where Marks >80;'
    cur.execute(query)
    data = cur.fetchall()
    print("Values has been added to the table")
    print()
#question no.4
    print("<--------solution 4-------->")
    print()
    print("Students with marks more than 80 are:")
    if len(data) is 0:
        print("There are no Student with marks grater than 80")
    else:
        for Name in data:
            print(Name[0])
    

finally:
    con.close()
    print('DONE!!')
