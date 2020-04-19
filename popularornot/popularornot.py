import re

print ("--------------------\n")
print ("Boy: boy\n")
print ("Girl: girl\n")
print ("Both: both\n")
print ("--------------------\n")
choose = input("Which one do you search in txt file? Boy or Girl or Both?\n\n") #input value


if choose == "boy": #if the input value is boy
    inputForBoy = input("\nEnter the Boy Name: ") #input value for boy name
    boyNames =open('BoyNames.txt','r') #open and read the txt file
    i=0
    for line in boyNames.readlines(): #searching each line 
        if re.match(inputForBoy + '$', line, re.I): #if the input value match in txt file
            i+=1 #value of i will be 1
    if i==1: #if i equals to 1
        print (inputForBoy ," was a popular boy's name between 2000 and 2009.") #print
    else: #else
        print (inputForBoy ," was not a popular boy's name between 2000 and 2009.") #print

elif choose == "girl":
    inputForGirl = input("Enter the Girl Name: ")
    girlNames =open('GirlNames.txt','r')
    i=0
    for line in girlNames.readlines():
        if re.match(inputForGirl + '$', line, re.I):
            i+=1
    if i==1:
        print (inputForGirl ," was a popular girl's name between 2000 and 2009.")
    else:
        print (inputForGirl ," was not a popular girl's name between 2000 and 2009.")


elif choose == "both":
    inputForBoy = input("Enter the Boy Name: ")
    inputForGirl = input("Enter the Girl Name: ")
    boyNames =open('BoyNames.txt','r')
    girlNames =open('GirlNames.txt','r')
    i=0
    j=0
    for line in boyNames.readlines():
        if re.match(inputForBoy + '$', line, re.I):
            i+=1
    if i==1:
        print (inputForBoy ," was a popular boy's name between 2000 and 2009.")
    else:
        print (inputForBoy ," was not a popular boy's name between 2000 and 2009.")
    
    for line in girlNames.readlines():
        if re.match(inputForGirl + '$', line, re.I):
            j+=1
    if j==1:
        print (inputForGirl ," was a popular girl's name between 2000 and 2009.")
    else:
        print (inputForGirl ," was not a popular girl's name between 2000 and 2009.")
            
