def function1(text):
    return text + text

def function2(text):
    return text.title()

output = function1("Hello")
print(output)

# what if we take the output of function1 and use it as an input into function2

out = function2(function1("hello"))
print(out)

# multiple return value:

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}, {formated_l_name}"
    #return f"result:" JUST RETURN result:

output = format_name(input("enter a f_name: "), input("enter a l_name: "))
print(output)
# ====================================================

def name_format(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you did not provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}, {formated_l_name}"

output = name_format(input("enter a f_name: "), input("enter a l_name: "))
print(output)

# return none
#=======================================================================
