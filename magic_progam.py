# THE MAGIC PROGRAM!!
print()
# ask user to pick a whole number between 1-31
print()
print("==========================================================================================")
print("Hello! I am the AMAZING HouPYni, I am going to read your mind!")
print()
print()
print("Please pick a whole number between 1 and 31, write it down and")
print("show it to your friends, but be careful not to let your phone or")
print("webcam see it, I want you to be sure that you have not been 'duped'.")
print()
print()
print("I am going to show you five tables of numbers. After each table, please input a 'Y' or")
print("an 'N' to symbolize whether or not your number was in the table.('Y' for Yes 'N' for No.)")
print("==========================================================================================")
print()

# define my tables and get user input after them
# had to create tables from scratch because tabulate would not work
table_1 = ("|1....3....5.....7|\n|9....11...13...15|\n|17...19...21...23|\n|25...27...29...31|") 
table_2 = ("|2....3....6.....7|\n|10...11...14...15|\n|18...19...22...23|\n|26...27...30...31|")
table_3 = ("|4....5....6.....7|\n|12...13...14...15|\n|20...21...22...23|\n|28...29...30...31|")
table_4 = ("|8....9....10...11|\n|12...13...14...15|\n|24...25...26...27|\n|28...29...30...31|")
table_5 = ("|16...17...18...19|\n|20...21...22...23|\n|24...25...26...27|\n|28...29...30...31|")

# user needs to select an appropriate response to start the trick
# question to start the trick should be asked as many times as it takes
# to recieve an appropriate answer.
blow_minds = ("y")
print("***********************************************************************")
while input("When you are ready to have your mind blown, please enter 'Y': ").lower() != (blow_minds):
    print()
    print("Y would You trY that?")
    print("Y don't we trY this again?")
    print()    
else:
    print()
    print()
    print(table_1)
    print()
    input_1 = input("Is your number on this ^^ table?: ")

# ask user for their answer on each of the tables 2-5    
print()
print(table_2)
print()
input_2 = input("How about this ^^ one?: ")
print()

print()
print(table_3)
print()
input_3 = input("And this ^^ one?: ")
print()

print()
print(table_4)
print()
input_4 = input("What about this ^^ one?: ")
print()

print()
print(table_5)
print()
input_5 = input("Last but not least, this ^^ one?: ")
print()


# guestimate will be what we think the users number is based on our algorithm
# guestimate can be any whole number from 1-31
# we need to be able to add each tables first number if the table was chosen by the user

# in order to throw the user off and bring down their guard for a bigger reveal
# we will add up the opposite of what they put in first and act as though that
# is their number, then we will give them their number

# define my inputs from the user about the 5 diff tables
# I need to take a y or n from each input and put that into an equation
guestimate = 0
fake_guestimate = 1

if input_1.lower() == ("y"):
    guestimate = (guestimate + 1)
else:
    fake_guestimate = (fake_guestimate + 1)

if input_2.lower() == ("y"):
    guestimate = (guestimate + 2)
else:
    fake_guestimate = (fake_guestimate + 2)

if input_3.lower() == ("y"):
    guestimate = (guestimate + 4)
else:
    fake_guestimate = (fake_guestimate + 4 )

if input_4.lower() == ("y"):
    guestimate = (guestimate + 8)
else:
    fake_guestimate = (fake_guestimate + 8)    
if input_5.lower() == ("y"):
    guestimate = (guestimate + 16)
else:
    fake_guestimate = (fake_guestimate + 16)    

# print the fake for dramatic tension
print()
print("***************************************************************************************")
print(f"HA! I got it! Was this your card...erm...Number? ***|||||||{fake_guestimate}|||||||***")
print("***************************************************************************************")
print()
print()
print()
print()

print("No?....Really?? Are you Sure???")
print(""" 




""")
print()
print("Oh, sorry, I forgot to turn on my 'left brain' scanner.")
print()
print("""





""")
print()
print()
print()
print()
# BIG reveal
print()
print(f"Haha, just kidding, there is no such thing as a left brain scanner,\n I scan the whole thing at one time...{guestimate}...")
print()



