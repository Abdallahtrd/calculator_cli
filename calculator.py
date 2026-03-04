history = []
def collect_number(): #This function collects the number from the user
    while True:
        try:
            number = float(input("Input number "))
            return number
        except ValueError:
            print("Invalid input!!!")

def operation_list():#This prints out the list of operators
    print("Your operators are..")
    print("+")
    print("-")
    print("*")
    print("/")
    
def collect_operation():#This collects the operator choice and returns the value.
    while True:
        operator = input("PICK AN OPERATOR ")
        return operator

def calculation(first_number, second_number, operator):#This is the processor function that 
    #does all the calculations based on choice and appends each calculation into history 
    # then returns the answer. 

        if operator == '+':
            result = first_number + second_number
            
        elif operator == '-':
            result = first_number - second_number
            
        elif operator == '*':
            result = first_number * second_number
               
        elif operator == '/': 
            result = first_number / second_number
                
        else:
             print("Invalid operation")
        
        record = f"{first_number} {operator} {second_number} = {result:.2f}"
        history.append(record)  

        return result  
        
        
        
def main():#The main function orchrestrates the logic and the arrangement of how their run.

    first_number = collect_number()
    second_number = collect_number()
    operation_list()
    operator = collect_operation()
    result = calculation(first_number, second_number, operator)
    print(result)

main()#In order for it to be like a real calculator it is assumed that the moment you run
#you do not need to be asked if you want to make a calculation, that is why main is being called
#here once before the loop


while True:#This loop makes it run infinitely until told to stop.s
    run_choice = input("Choose: (C)alculation, (H)istory, (Q)uit: ").lower()
    if run_choice == 'c':
        main()#Main is called here for enable calculation after choice.

    elif run_choice == 'h':#Added the history choice in menu selection.
        for index, record in enumerate(history, start=1):
            print(f"{index}. {record}") 

    elif run_choice == 'q':
        break
    else:#This is the part that asks the user again after an invalid input in run_choice. 
        print("Invalid Input")
        continue #continue takes the user back to the beginning of the loop instead of ending the program.
    
        
    