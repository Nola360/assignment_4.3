#Akinola Daramola Jr
#Programming Exercise 4.3
#Due Date: 06/26/2022


"""
Budget Analysis
Write a program that asks the user to enter the amount that he or she has budgeted for a month.
A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.
When the loop finishes, the program should display the amount that the user is over or under budget.
"""

#Initializing value of budget and expense variable
budget = 0.0
expenses = 0.0

#Declaring value of budget amount
budget = float(input("Enter monthly budget: "))

#Declaring value of budget total
budget_total = budget

#Declaring value of expense total
expense_total = expenses

#Displaying monthly budget
print(f"Monthly budget: ${budget_total:,.2f}") 

#Declaring value of spend variable
spend = True

while spend is True:  #Loop start
    expenses = float(input("Enter expense for month: "))    #Declaring value of expense amount 
    budget_total = budget_total - expenses          #Calculating budget total after expenses
    print(f"Total budget: ${budget_total:,.2f}")    #Printing new budget
    expense_total = expense_total + expenses        #Calculating expense total
    print(f"Total expense: ${expense_total:,.2f}")  #Printing expense total
    if budget_total < budget:                       #Conditional Statement
        message = input("Continue Y/N? ")           #Usability feature
        if(message == "n" or message == "N") and expense_total > budget:    #Functions when users selects no and expense amount exceeds than budget 
            amount_over_budget = expense_total - budget                     #Calculates total amount exceeding budget
            print(f"Monthly budget: ${budget:,.2f}")        #Displays initial budget amount
            print(f"Total expense: ${expense_total:,.2f}")  #Displays running total of expense amount
            print(f"Amount over budget: ${amount_over_budget:,.2f}")    #Displays amount over budget
            spend = False #Stops Loop
        elif (message == "n" or message == "N") and expense_total >= budget_total: #Functions when user selects no and budget total is less than or equal to expense total
            print(f"Monthly budget: ${budget:,.2f}")            #Shows initial budget amount
            print(f"Total expense: ${expense_total:,.2f}")      #Printing expense total
            print(f"Budget available: ${budget_total:,.2f}")    #Displays budget amount remaining
            spend = False #Stops Loop
        else:
            print("Continue") #Confirms user selection
