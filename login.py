#here we are importing mysql connector
import mysql.connector as a 
#here we are importing repeat function from base file 
from base import repeat

#This is used to connect to my database
con=a.connect(user='root',host='localhost',password='Aravind@9848',database='bank')
c=con.cursor(buffered=True)

"""
       This login function has two input parameters 
        1.Username
        2.Password
       
       Once the user is logged in ,They can access various
       functions .
       
       Functions available are : 
          1.Account Information
          2.List Benificiary
          3.List of cards
          4.Add Benificiary
          5.Register New Credit Card
          6.Change Pin
          7.Update Information
          8.Transfer Funds 
"""
def login():
    n=input("Enter your username : ")
    sql='select username from registered' #sql query to check weather required username is present in the database 
    var=()
    c.execute(sql,var)
    result=c.fetchall()
    """
       Here we are going to verify weather the username
       is registerd or not and throws an error if it is not found
       
    """
    I=[]
    for i in result:
        I.append(i[0])
    temp=n in I 
    while temp==False:
        print("This username is not registered  ")
        print("Please try again ")
        n=input("Enter your username : ")
        temp=n in I    
    #Once username is confirmed it will ask for password    
    print("Thank you for confirming the username ")   
    
    while True:
        
        #we have to enter password here 
        n1=input("Enter your  password : ")
        
        sql5 = "select md5(%s)"
        var5 = (n1,)
        c.execute(sql5,var5)
        encpw = c.fetchone()[0]
        
 
        sql1='select paswrd from registered where username = (%s)'
        var1=(n,)
        c.execute(sql1,var1)
        result2=c.fetchone()[0]
        
        """
        Here we will verify weather the password matches 
        with the one given while registration .
       
        If it matched then we can see various options available to us 
        Otherwise we get an error to check the password .
        """ 
        tempp=result2==encpw
        if tempp==False:
            print("Entered password is Incorrect ")
            print("Please try again ")
        
             
        else:
            print("Thanks for logging in ") 
            break
    
    repeat()


