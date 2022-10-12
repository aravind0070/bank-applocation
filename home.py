#imports mysql connector
import mysql.connector as a
#importslogin function from login file 
from login import login
#imports register function from registration file
from registration import register

#These are used to connect to your data base 
con=a.connect(user='root',host='localhost',password='Aravind@9848',database='bank')
c=con.cursor(buffered=True)


def main():
    print("""
          1.Registration
          2.Login
        """)
    """
       Here the user will select from the
       given options which they desire 
    """
    choice =input("Enter task no : ")
    if(choice=='1'):
        register()
    elif(choice=='2'):
        login() 
             
    else:
        print("wrong choice :")
        main()


#Code execution starts from here 
main()                  
