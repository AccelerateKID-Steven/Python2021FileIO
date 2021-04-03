#Steven Kalis
#2/27/2021
#Intro to File I/O
#The program will open a file, search for a word, and replace
#that word with something else

#in order to use reletive file pathing, we need 
# to import the os module
#re will give us the sub function
import os, re
fileDir = os.path.dirname(__file__)
txtInFile = []

#look through file, 
#checking to see if it is found, also
#counting how many times the word appears
#If found, asks to replace that word with another
#if not found, asks if you would want to find another word




found = False
while not found:
    theWord = input("Search for a word:")
    #check if the word is just one word
    #how? by checking to see if it has a space
    #loop through the string looking for the ' '

    #Way #1 of opening a file: to open a file, we use the open function
    #with open(fileDir + "\\text\\fileIO.txt","r") as file:
        #work with the file
    #    txtInFile = file.readline()
    #Way #2 of opening a file, makes the file a variable 
    # HAVE TO CLOSE WHEN DONE
    file = open(fileDir + "\\text\\FileIO.txt","r")

    #convert file into array
    txtInFile = file.readlines()

    
    
    file.close()
    #clears the file
    open(fileDir + "\\text\\FileIO.txt","w").close()
    
    isThere = False
    count = 0
    for line in txtInFile:
        
        if (not line.lower().find(theWord.lower()) == -1) and isThere == False:
            #print("YEP: " + line)
            isThere = True
            count += 1
        elif (not line.lower().find(theWord.lower())) == -1 and isThere == True:
            #print("YEP: " + line)
            count += 1
        
        

    if count > 0:
        found = True
        print("The word was found " + str(count) + " time(s)")
        changeTo = input("What would you like to change '" + theWord + "' to?")
        for i in range(len(txtInFile)):
            if not txtInFile[i].lower().find(theWord.lower()) == -1:
                currentLine = txtInFile[i]
                #TODO The way we read it isnt right
                txtInFile[i] = re.sub(theWord,changeTo,currentLine)
        file = open(fileDir + "\\text\\FileIO.txt","a")
        for i in range(len(txtInFile)):
            file.write(txtInFile[i])
        file.close()
    else:
        print("The word was not found :(")

    





