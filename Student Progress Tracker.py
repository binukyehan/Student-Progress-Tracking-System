# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20527837
# Date: 13/12/2023

Creditslist = [] #Decalre a list to get the Credits.
Outcomelist = [] #Declare a list to get the Outcomes.
f = open("Progression data.txt","w") #Creating a text file.
f.write("\nPart 3 - Text file(extension)\n") #Entering the topic of the text file.
f.close()


def CreditsInput(): #Take the Pass,Defer,Fail credit values from the user.
    '''Gets the Pass, Defer and Fail inputs from the user

Checks if the values are in range
Checks if the entered value is an integer
Checks if the total is correct

and shows a custom error message if any error occurs.'''
    global Pass, Defer, Fail
    try:
        Pass = int(input("\nPlease enter your credits at pass : "))
        if Pass not in range(0,121,20): #Checking if the entered value is within the range.
            print("Out of range.")
            main()
        Defer = int(input("Please enter your credits at defer : "))
        if Defer not in range(0,121,20):
            print("Out of range.")
            main()
        Fail = int(input("Please enter your credits at fail : "))
        if Fail not in range(0,121,20):
            print("Out of range.")
            main()
    except ValueError: #Avoiding displaying of value error 
        print("Your input should be an integer.")
        main()
    if Pass + Defer + Fail != 120: #Checking if the total is correct.
        print("Total incorrect.")
        main()
    return Pass
    return Defer
    return Fail

        
def main():
    '''Gets the Pass, Defer, Fail values from the CreditsInput() function,
calculates the outcome of the student and displays it.

Temporary add the credits values of the current student to Credistlist 
Save the outcome of each student to a list called Outcomelist
Add those out comes of each student to the "Progression data" text file as well

After the Cont() function runs,
    Show the results of students taking the values from Outcomelist.
    Show the results of students taking the values from the text file as well.

Then exits the program when the user presses "Enter" key.'''
    global ProgressCount, ExcludeCount, Module_trailerCount, Module_retrieverCount
    global Pass, Defer, Fail
    global Creditslist, Outcomelist
    Creditslist = [] #Clearing the list to get the new values.
    CreditsInput() #Getting the input values to the main() function
    Result = ''
    if Pass == 120: #Calculating the outcome.
        Result = 'Progress'
        ProgressCount += 1
    elif Fail >= 80:
        Result = 'Exclude'
        ExcludeCount += 1
    elif Pass == 100:
        Result = 'Progress(Module trailer)'
        Module_trailerCount += 1
    elif Pass <= 80:
        Result = 'Do not progress(Module retriever)'
        Module_retrieverCount += 1
    print("Your result is :",Result) #Showing the outcome.
    Creditslist.append(Pass) #Passing the credit values to Creditslist.
    Creditslist.append(Defer)
    Creditslist.append(Fail)
    Outcomelist.append(f"{Result} - {Creditslist[0]}, {Creditslist[1]}, {Creditslist[2]}")#Passing the result values with the credit values to Outcomelist.
    f = open("Progression data.txt","a") #Open the text file to apppend.
    f.write(f"{Result} - {Creditslist[0]}, {Creditslist[1]}, {Creditslist[2]}\n")
    f.close()
    Cont()
    print("\n\nPart 2 - List(extension)") 
    for results in Outcomelist: #Showing each outcome with the corresponding credit values.
        print(results)
    f = open("Progression data.txt","r") #Open the text file to read.           
    for data in f.readlines(): #Read the text line by line.
        print (data.strip())
    f.close()
    input("\nPress enter to exit.")
    quit()

    
def Cont():
    '''Asks whether the user wants to continue to add another set of credits or
if they want to quit the program to see the histogram results'''
    Continue = input("\nDo you want to continue? (q/y) : ") #Gets the value from user asking if they want to continue.
    if Continue.lower() == "q": 
        Histogram() #Calls Histogram() function if the user enters "q".
    elif Continue.lower() == "y":
        main() #Calls main() function if the user enters "y"
    else:
        print("Incorrect input.") #Shows an error message if user enters a character that is not "q" or "y".   
        Cont()

        
from graphics import *
def Histogram():
    '''Creates the histogram and displays it on a seperate window,
showing the number of students for each type of outcome.'''
    global ProgressCount, ExcludeCount, Module_trailerCount, Module_retrieverCount
    win = GraphWin("Histogram Results", 700, 600) #Open the window and name it as "Histogram Results".
    win.setBackground(color_rgb(250,248,235))#Set the background colour of the window.
    lineX = Line(Point(100,500),Point(600,500)) #x axis of the histogram
    lineY = Line(Point(100,500),Point(100,100)) #y axis of the histogram
    lineX.setArrow("last") #Adding arrow-heads.
    lineY.setArrow("last")
    Title = Text(Point(350,70),"Histogram Results") #Add the title
    Title.setSize(16) #Set the font size of the title.
    Title.draw(win)
    info = Text(Point(200,560),f"Total no. of outcomes : {ProgressCount+Module_trailerCount+Module_retrieverCount+ExcludeCount}") #Displaying total no. of outcomes
    info.draw(win)
    Outcome1Bar = Rectangle(Point(150,500),Point(200,500-ProgressCount*20)) #Creating the coloumns for each Outcome type, with the height depending on the outcome count.
    Outcome2Bar = Rectangle(Point(250,500),Point(300,500-Module_trailerCount*20))
    Outcome3Bar = Rectangle(Point(350,500),Point(400,500-Module_retrieverCount*20))
    Outcome4Bar = Rectangle(Point(450,500),Point(500,500-ExcludeCount*20))
    Outcome1Count = Text(Point(175,490-ProgressCount*20),ProgressCount) #Displaying the number of outcomes for each type of result.
    Outcome2Count = Text(Point(275,490-Module_trailerCount*20),Module_trailerCount)
    Outcome3Count = Text(Point(375,490-Module_retrieverCount*20),Module_retrieverCount)
    Outcome4Count = Text(Point(475,490-ExcludeCount*20),ExcludeCount)
    Outcome1Count.draw(win)
    Outcome2Count.draw(win)
    Outcome3Count.draw(win)
    Outcome4Count.draw(win)
    Outcome1 = Text(Point(175,515),"Progress") #Creating label for each outcome.
    Outcome2 = Text(Point(275,515),"Trailer")
    Outcome3 = Text(Point(375,515),"Retriever")
    Outcome4 = Text(Point(475,515),"Excluded")
    Outcome1.draw(win)
    Outcome2.draw(win)
    Outcome3.draw(win)
    Outcome4.draw(win)
    Outcome1Bar.setFill(color_rgb(91,114,181)) #Setting the colour of the columns using the RGB method.
    Outcome2Bar.setFill(color_rgb(181,91,91))
    Outcome3Bar.setFill(color_rgb(170,181,91))
    Outcome4Bar.setFill(color_rgb(181,147,91))
    lineX.draw(win)
    lineY.draw(win)
    Outcome1Bar.draw(win)
    Outcome2Bar.draw(win)
    Outcome3Bar.draw(win)
    Outcome4Bar.draw(win)
    try:
        win.getMouse() #Waiting for a mouse click for the window to close.
        win.close()
    except GraphicsError: #Avoiding the error that shows if the user closes the window using close button.
        pass
    
global ProgressCount, ExcludeCount, Module_trailerCount, Module_retrieverCount 
ProgressCount = 0
ExcludeCount = 0
Module_trailerCount = 0
Module_retrieverCount = 0

main() #Calling the main() function
 
