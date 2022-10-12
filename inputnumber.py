"""
   This function is used to check 
   weather the given input is integer 
   or not .
"""


def inputNumberr(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
      """
        This error is shown if the
        entered value is not an integer
       """
      print("Not a valid input! Try again.")
      continue
    else:
       return userInput 