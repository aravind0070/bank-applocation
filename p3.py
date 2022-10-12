#I have imported mysql connector,pandas and connection for multiprocessing
from multiprocessing import connection
import re
from xml.dom.domreg import registered
import mysql.connector as a 
import pandas as pd
import re
from registration import *
from registration import register
from carddetails import usercards


#mysql
#These are my details to connect to my database
con=a.connect(user='root',host='localhost',password='Aravind@9848',database='bank')
c=con.cursor(buffered=True)

def run(string):
 
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:;,.+=-`]')
     
    # Pass the string in search
    # method of regex object.   
    if(regex.search(string) == None):
        return False
         
    else:
        return True
        
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not a valid input! Try again.")
       continue
    else:
       return userInput 
#this is space function
def space(str):
    s=str
    flag = False
    for a in s:
        if(a.isspace())==True:
          flag = True
          break
        else:
          exit
    return flag
#this is a repeate function
def repeat():
      
    print("""
          1.Account Information
          2.List Benificiary
          3.List of cards
          4.Add Benificiary
          5.Register New Credit Card
          6.Change Pin
          7.Update Information
          8.Transfer Funds 
          
          """)
    choice =input("Enter task no : ")
    if(choice=='1'):
         getinfo()
    elif(choice=='2'):
         beni() 
    elif(choice=='3'):
        cards()
    elif(choice=='4'):
        addben()    
    elif(choice=='5'):
        new() 
    elif(choice=='6'):
        change()
    elif(choice=='7'):
        update() 
    elif(choice=='8'):
        transfer()
    # elif(choice=='9'):
    #     main()
    else:
        print("wrong choice ") 
        print("select option again") 
        repeat()

def recal():
    print('''
          1.Now add your card details :
          
             ''')
    ch=input("Enter task number : ")
    if(ch=='1'):
      usercards()
    else:
        print("Wrong input , please try again ")
        recal()
#user registration happens here 
#what all details user enters will get stored in registered table 


#Different cards which each user has  
#tesing git   
# #commenting
# def usercards():
    # while True:
    #     n=input("Enter username : ")
    #     f = space(n)
    #     if f is True:
    #         print("Spaces cannot be there in the input")
    #         pass
    #     else:
    #         break
   
#     while True:
#         n1=input("Enter card Type :")
#         a="credit"
#         b="debit"
#         if(n1!=a and n1!=b):
#           print("Enter a valid card type")
#           pass
#         else:
#             break
        
   
#     while True:
#         n2=input("Enter card name :")
#         tmp=run(n2)
#         if(tmp==False):
#             break
#         else:
#             print("Special charecters not allowed")
#             pass
#     while True:
#         n3=inputNumber("Enter card Number:")
#         k=str(n3)
#         d=len(k)
#         if(d!=16):
#           print("Check for 16 digits in card number ")
#           pass
#         else:
#             break
#     while True:
#         n4=inputNumber("Enter card pin :")
#         e=str(n4)
#         f=len(e)
#         if(f!=4):
#           print("Check for 4 digits in card pin ")
#           pass
#         else:
#             break
#     while True:
#         n5=inputNumber("Enter card cvv :")
#         a=str(n5)
#         b=len(a)
#         if(b!=3):
#           print("Check for 3 digits in cvv")
#           pass
#         else:
#             break        
    
    
   
#     n6=inputNumber("Enter card balance  :")
    
    
#     print("Card details updated Succesfully !!")
#     print("Now you can Login")
#    # login()
#     data2=(n,n1,n2,n3,n4,n5,n6)
#     sql2='insert into usercards  values(%s,%s,%s,%s,%s,%s,%s)'
    
#     c.execute(sql2,data2)
#     con.commit()
# teting github
##this is a code for logging in      
# def login():
#     n=input("Enter your username : ")
#     sql='select username from registered'
#     var=()
#     c.execute(sql,var)
#     result=c.fetchall()
#     I=[]
#     for i in result:
#         I.append(i[0])
#     temp=n in I 
#     while temp==False:
#         print("This username is not registered  ")
#         print("Please try again ")
#         n=input("Enter your username : ")
#         temp=n in I    
#     print("Thank you for confirming the username ")   
    
#     while True:
        
#         n1=input("Enter your  password : ")
        
#         sql5 = "select md5(%s)"
#         var5 = (n1,)
#         c.execute(sql5,var5)
#         encpw = c.fetchone()[0]
        
#         sql1='select paswrd from registered where username = (%s)'
#         var1=(n,)
#         c.execute(sql1,var1)
#         result2=c.fetchone()[0]
        
#         tempp=result2==encpw
#         if tempp==False:
#             print("Entered password is Incorrect ")
#             print("Please try again ")
        
             
#         else:
#             print("Thanks for logging in ") 
#             break
    
#     repeat()
       
    
#To get the information of desired user
def getinfo():
    k=input("Confirm the username to get information : ")
    d=(k,)
    sql_command='''  select registered.username ,registered.address,registered.adharnumber,registered.mobilenumber , usercards.cardtype , usercards.cardname , usercards.cardbalance from registered INNER JOIN usercards ON registered.username = usercards.username WHERE usercards.username= %s '''
    c.execute(sql_command,d)
    result = c.fetchall()
    det = ['[username]','[address]','[adhar number]','[ph number]','[card type]','[card name]','[card balance]']
    print("")
    print('-'*115)
    print('| {:^12} | {:^12} | {:^15} | {:^12} | {:^15} | {:^10} | {:^10}  |'.format(*det))
    print('-'*115)
    for i in result:
        print('| {:^12} | {:^12} | {:^15} | {:^12} | {:^15} | {:^10} | {:^10}       |'.format(*i))
        print('-'*115)
   
    con.commit()
    con.close()
    repeat()
    
#To see all the benificiary names for a user
def beni():
    k=input("Confirm the username , to know the beneficiaries : ") 
    d=(k,)
    sql_command=''' select * from benificiary where username=%s '''  
    c.execute(sql_command,d)
    result = c.fetchall()
    det=['[username]','[benificiary]']
    print("")
    print('-'*32)
    print('| {:^10} | {:^15} |'.format(*det))
    print('-'*32)
    
    if result:
        for i in result:
            print('| {:^10} | {:^15} |'.format(*i))     
            print('-'*32) 
        
       
    else:
        print("There are no beneficiaries")
       
    
    con.commit()
    con.close()  
    repeat()   

#To see what all cards each user has 
def cards():
    k=input("Enter the username for whom u want to see card details ")
    d=(k,)
    sql_command=''' select cardtype,cardname from usercards where username=%s '''  
    c.execute(sql_command,d)
    result = c.fetchall()
    det=['[card type]','[card name]   ']
    print("")
    print('-'*32)
    print('| {:^10} | {:^12}   |'.format(*det))
    print('-'*32)
    
    if result:
        for i in result:
            print('| {:^10} | {:^15} |'.format(*i))     
            print('-'*32)
    
    
    con.commit()
    repeat()
#To add benificiary names
def addben():
    n=input("Confirm the  username : ")
    n1=input("Enter benificary name : ")
    data=(n,n1)
    sql='insert into benificiary values(%s,%s)'
    print("Benificiary added succesfully! ")
    
    c.execute(sql,data)
    con.commit() 
    repeat()   

#To add new card details into usercards table
def new():
    
    while True:
        n=input("Enter username : ")
        f = space(n)
        if f is True:
            print("Spaces cannot be there in the input")
            pass
        else:
            break
   
    while True:
        n1=input("Enter card Type :")
        a="credit"
        b="debit"
        if(n1!=a and n1!=b):
          print("Enter a valid card type")
          pass
        else:
            break
        
    
    while True:
        n2=input("Enter card name :")
        tmp=run(n2)
        
        if(tmp==False):
            break
        else:
            print("Special charecters not allowed")
            pass
    
   
    while True:
        n3=inputNumber("Enter card Number:")
        k=str(n3)
        d=len(k)
        if(d!=16):
          print("Check for 16 digits in card number ")
          pass
        else:
            break
    
    while True:
        n4=inputNumber("Enter card pin :")
        e=str(n4)
        f=len(e)
        if(f!=4):
          print("Check for 4 digits in card pin ")
          pass
        else:
            break
    
    while True:
        n5=inputNumber("Enter card cvv :")
        a=str(n5)
        b=len(a)
        if(b!=3):
          print("Check for 3 digits in cvv")
          pass
        else:
            break   
    
    n6=inputNumber("Enter card balance  :")
    data2=(n,n1,n2,n3,n4,n5,n6)
    sql2='insert into usercards  values(%s,%s,%s,%s,%s,%s,%s)'
    print("New card has been added to the database!")
    
    c.execute(sql2,data2)
    con.commit()
    repeat()

#To change pin 
def change():
   
    while True:
        n=inputNumber("Enter new card pin :")
        e=str(n)
        f=len(e)
        if(f!=4):
          print("Check for 4 digits in card pin ")
          pass
        else:
            break
   
    while True:
        n1=input("Enter username : ")
        f = space(n1)
        if f is True:
            print("Spaces cannot be there in the input")
            pass
        else:
            break
   
    while True:
        n2=input("Enter card Type :")
        a="credit"
        b="debit"
        if(n2!=a and n2!=b):
          print("Enter a valid card type")
          pass
        else:
            break
        
    while True:
        n3=input("Enter card name :")
        tmp=run(n3)
        
        if(tmp==False):
            break
        else:
            print("Special charecters not allowed")
            pass
    
    data=(n,n1,n2,n3)
    sql='''UPDATE usercards SET  cardpin=%s WHERE username=%s AND  cardtype =%s AND  cardname=%s '''
    print("Card pin is updated!")
   
    c.execute(sql,data)
    con.commit()
    repeat()
    # UPDATE myTable SET myValue = NULL WHERE myValue = '0';
    
#to UPDATE the records of a user 
def update():
    
    n=input("Enter the Address : ")
   
    while True:
        n1=inputNumber("Enter the Phone Number : ")
        a=str(n1)
        b=len(a)
        if(b!=10):
          print("Check for 10 digits in the number ")
          pass
        else:
            break
    n2=input("Confirm whose details you want to update : ")
    data=(n,n1,n2)
    sql=''' UPDATE registered SET address= %s ,mobilenumber= %s WHERE username= %s '''
    print("The details have been updated!")
    
    c.execute(sql,data)
    con.commit()
    repeat()

#TO transfer funds 
def transfer():
   
    n1=inputNumber("Enter card number from whom you want to transfer funds : ")
    
    sq='''select cardnumber from usercards'''
    var=()
    c.execute(sq,var)
    result=c.fetchall()
    l=[]
    for i in result:
        l.append(i[0])
    temp = n1 in l
    while temp==False:
      print("Not a valid card number or card number not registered")
      cd=input("Enter the cardnumber : ")
      temp = n1 in l
    print("Thank you for conforming the card number....")
    
    
    n2=inputNumber("Enter  the amount you want to transfer : ")
    n3=inputNumber("Enter reciever's card number : ")
    
    temp = n3 in l
    while temp==False:
      print("This reciever cardnumber has not been registered.......")
      cd=input("Enter the cardnumber : ")
      temp = n3 in l
    print("Thank you for conforming the recivers card number....")
   
    data=(n2,n1)
    data1=(n2,n3)
    sql=''' UPDATE usercards SET cardbalance=cardbalance- %s where cardnumber= %s '''    
    sql1=''' UPDATE usercards SET cardbalance=cardbalance+%s where cardnumber=%s'''
    print("Amount transfered succesfully !!")
    c.execute(sql,data)
   
    c.execute(sql1,data1)
    con.commit()
    repeat()
     
