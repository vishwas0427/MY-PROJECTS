import mysql.connector
db = mysql.connector.connect(host = "localhost",password = "root",user = "root",database = "predator")
cur = db.cursor()
print(" 1.Registarion \n2.Login Page ")
while (True):
    Choice = int(input(" Enter your choice : "))   
    if Choice == 1:
        Name = input(" Enter a name : ")
        Contact = int(input(" Enter a contact number : ")) 
        Gmail = input(" Enter a gamil Id : ")
        Salary = int(input(" Enter a salary amount : "))   
        Address = input(" Enter a address :")
        Password = input(" Enter a password : ")
        cur.execute("insert into Registration (name,contact,gmail,salary,address,password) values (%s,%s,%s,%s,%s,%s)",(Name,Contact,Gmail,Salary,Address,Password))
        db.commit()
        print("Registartion successful")
    elif    Choice == 2:
        Name = input(" enter your name : ")
        Password = input(" enter your password ")
        #cur.execute("select Name ,Password from registration where name = (%s,%s)",(name,password))
        #cur.execute("select * from registration")
        cur.execute("select name password from Registration where name = %s",(Name,))
        #a = cur.fetchmany()
        
        #print(" login successful : ")
        for i in cur:
            print(i)
            if Name in i:
                print("login successfull")
            else :
                print("login unsuccessful")