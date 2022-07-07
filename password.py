# i wasnt sure of yje syntax for checking for three conditions our of four and used a stackoverflow example
# https://stackoverflow.com/questions/22240396/logic-to-test-that-3-of-4-are-true

#Used exit() to end program if two of the requirements are not met. I learnt I had to import sys to stop program from running
# https://www.edureka.co/community/21051/how-to-exit-a-python-script-in-an-if-statement

#I wanted to use funtions to make blocks less repetitive but I got stuck 

#*************** Compulsory Task 1 ***************
# A program that ensures certain conditions are met for an internet password to be strong
import sys
have_length = False
up_case = False
low_case = False
have_num = False


#Ensure length of password meets set standard of 6 characters
long_enough = input("Is the password length atleast 6 characters long? Enter 'yes' or 'no': ").lower()
if (long_enough == "yes"):
        have_length = True

#Check if password contains uppercase letters
up_caps = input("\nDoes the password contain any uppercase letters? Enter 'yes' or 'no': ").lower()
if (up_caps == "yes"):
        up_case = True
        
elif [have_length, up_case].count(False) == 2:
        print("\nThe password is not suitable")
        sys.exit()
        
#Check if password contains lowercase letters
low_caps = input("\nDoes the password contain any lowercase letters? Enter 'yes' or 'no': ").lower()
if (low_caps == "yes"):
        low_case = True

elif [have_length, up_case, low_case].count(False) == 2:
        print("\nThe password is not suitable")
        sys.exit()

if [have_length, up_case, low_case, have_num].count(True) == 3:
        print("\nThis is a suitable password")

#Check if password contains numnerinc characters
elif [have_length, up_case, low_case, have_num].count(True) != 3:        
        numerics = input("\nDoes the password contain any numbers? Enter 'yes' or 'no': ").lower()
        if (numerics == "yes"):
            have_num = True
        if [have_length, up_case, low_case, have_num].count(True) == 3:
            print("\nThis is a suitable password")
        else:
            print("\nThe password is not suitable") 
        
                
