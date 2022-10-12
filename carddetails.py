#we are importing inputnumberr function from inputnumberfile 
from inputnumber import inputNumberr
#we are importing regex 
import re as re
#we are importing mysql connector 
import mysql.connector as a 



#These are used to connect to the data base 
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
    """
      This function checks for spaces 
      in the  given input string and 
      throws out an error if found 
    """
    s=str
    flag = False
    for a in s:
        if(a.isspace())==True:
          flag = True
          break
        else:
          exit
    

def usercards():
    while True:
        #Here we take the username of the user who want to add card details 
        n=input("Enter username : ")
        f = space(n)
        if f is True:
            print("Spaces cannot be there in the input")
            pass
        else:
            break
   
    while True:
        """
            Here we enter the type of card they want to add
            Two options are provided 
            1.credit
            2.debit 
        """
        n1=input("Enter card Type :")
        a="credit"
        b="debit"
        if(n1!=a and n1!=b):
          print("Enter a valid card type")
          pass
        else:
            break
        
    """
        Here we have to enter the
        card name  and it shouldnt
        contain any special characters
    """
    while True:
        n2=input("Enter card name :")
        tmp=run(n2)
        if(tmp==False):
            break
        else:
            print("Special charecters not allowed")
            pass
    """
        Here we must enter the 16
        digit card number it must 
        be of all integers .
    """    
    while True:
        n3=inputNumberr("Enter card Number:")
        k=str(n3)
        d=len(k)
        if(d!=16):
          print("Check for 16 digits in card number ")
          pass
        else:
            break
    """
        Here we must enter the 16
        digit card number it must 
        be of all integers .
    """       
    while True:
        n4=inputNumberr("Enter card pin :")
        e=str(n4)
        f=len(e)
        if(f!=4):
          print("Check for 4 digits in card pin ")
          pass
        else:
            break
    """
        Here we must enter the 4
        digit card pin it must 
        be of all integers .
    """       
    while True:
        n5=inputNumberr("Enter card cvv :")
        a=str(n5)
        b=len(a)
        if(b!=3):
          print("Check for 3 digits in cvv")
          pass
        else:
            break        
    
    """
        Here we must enter the 3
        digit card cvv it must 
        be of all integers .
    """   
   
    n6=inputNumberr("Enter card balance  :")
    """
        Once all details are added they are added to the database.
    """   
    
    print("Card details updated Succesfully !!")
    print("Now you can Login")
   
    data2=(n,n1,n2,n3,n4,n5,n6)
    sql2='insert into usercards  values(%s,%s,%s,%s,%s,%s,%s)'
    
    c.execute(sql2,data2)
    con.commit()
    
