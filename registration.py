#we import mysql connector
import mysql.connector as a
#we import regex expression 
import re
#we have imported usercards functtion from carddetails file 
from carddetails import usercards
from inputnumber import inputNumberr

#here we connect to our data base 
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
            
def register():
    while True:
        n=input("Enter username : ")
        f = space(n)
        if n=='':
            print("Username cant be NULL")
            pass
        
        elif f is True:
            print("Spaces cannot be there in the input")
            pass
        else:
            break
    add=input("Enter address : ")
    
   
    while True:
        ad=inputNumberr("Enter Adhar Number : ")
        a=str(ad)
        b=len(a)
        if(b!=12):
          print("Check for 12 digits in the adhar number ")
          pass
        else:
            break
    
    while True:
        mb=inputNumberr("Enter 10 mobile number without country code : ")
        a=str(mb)
        b=len(a)
        if(b!=10):
          print("Check for 10 digits in the number ")
          pass
        else:
            break
    paw=input("Enter a password : ")
    
    data1=(n,add,ad,mb,paw)
    sql1='insert into registered values(%s,%s,%s,%s,MD5(%s))'
    print("Registration is succesfull !!")
    recal()
    
        
    c.execute(sql1,data1)
    con.commit()