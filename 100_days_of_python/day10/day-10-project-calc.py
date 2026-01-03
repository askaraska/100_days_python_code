import art

""" create function for four mathematical operations +,-,*,/ with parameter n1,n2 """
def add(n1, n2):
    return n1 + n2

#my_favourite_operation = add
#print(my_favourite_operation(2,3))

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

#todo-2: add these 4 functions into a dictionary as the values. key "+","-","*","/"

operations = {
    #assign function to key(variable) not triggering the function that means
    # if call that key(variable) that call function corresponding function
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}

#todo-3: use the dictionary operation to perform the calculation . multiply 4*8
# print(operations["*"](4,8))
def calculator():
    print(art.logo)
    should_accumulate = True #step8:
    #step1: ask num1 input from user , at step1 stage not consider about while loop
    num1 = float(input("what is your first number?: ")) #step9: put num1 variable before while loop
    while should_accumulate: #step8:
        # step2: for printing operation symbol :
        for symbol in operations: # operations refer dict
            print(symbol)
        # pick the operation symbol step2.1:
        operation_symbol = input("pick an operation: ")
        #step3:
        num2 = float(input("what is your second number?: "))
        #step4: start calculation by using dict
        # print(operations[operation_symbol](num1, num2))
        answer = operations[operation_symbol](num1, num2)
        print(f"{answer}")
        #step5:
        #need to show equation also:
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        #todo-4: program asks if user wants to continue working with previous result:
        #step6:
        choice = input(f"Type 'y' to continue with {answer} or type 'n' to new calculation: ")
        #step7:
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()