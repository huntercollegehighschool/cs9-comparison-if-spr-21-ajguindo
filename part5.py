'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below
#The months having 31 days in a year are January, March, May, July, August, October, and December.

month = input("Enter a month: ")

January = 31
March = 31
May = 31
July = 31
August = 31
October = 31
December = 31


if month == 31: 
  print("31")
elif month: 
  print("28 or 29")
elif month == March:
  print("30")
else:
  print("not a month")