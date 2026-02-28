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

def calculation(first_number, second_number, operator):#This is the processor function that does all the callculations based on choice and returns each one.

        if operator == '+':
            return first_number + second_number
        elif operator == '-':
            return first_number - second_number
    
        elif operator == '*':
            return first_number * second_number
    
        elif operator == '/':
            return first_number / second_number
        else:
             print("Invalid operation")

def main():#RThe main function orchrestrates the logic and the arrangement of how their run.

    first_number = collect_number()
    second_number = collect_number()
    operation_list()
    operator = collect_operation()
    result = calculation(first_number, second_number, operator)
    print(result)

main()#In order for it to be like a real calculator it is assumed that the moment you run
#you do not need to be asked if you want to make a calculation, that is why main is being called
#here once before the loop


while True:#This loop makes it run infinitely until told to stop.
    run_choice = input("Do you want to make a new calculation? y/n ").lower()
    if run_choice == 'y':
        main()#Main is called here for enable calculation after choice.
    elif run_choice == 'no':
        break
    else:#This is the part that asks the user again after an invalid input in run_choice. 
        print("Invalid Input")
        continue
    
        
    