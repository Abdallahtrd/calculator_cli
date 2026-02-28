def collect_number(): #This function collects the number from the user
    while True:
        try:
            number = float(input("Input number "))
            return number
        except ValueError:
            print("Invalid input!!!")

def operation_list():
    print("Your operators are..")
    print("+")
    print("-")
    print("*")
    print("/")
    
def collect_operation():
    while True:
        operator = input("PICK AN OPERATOR ")
        return operator

def calculation(first_number, second_number, operator):

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

def main():

    first_number = collect_number()
    second_number = collect_number()
    operation_list()
    operator = collect_operation()
    result = calculation(first_number, second_number, operator)
    print(result)


while True:
    main()
    run_choice = input("Do you want to make a new calculation? y/n ").lower()
    if run_choice == 'y':
        pass
    elif run_choice == 'no':
        break
    else:
        print("Wrong Input Please Try Again!!")
         
        
    