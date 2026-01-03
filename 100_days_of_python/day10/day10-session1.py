"""FUNCTIONS WITH OUTPUTS"""

def my_function():
    result = 3 * 6
    return result

output = my_function()
print(output)

#change title case of name:
# def format_name(f_name,l_name):
#     f_name.title()
#     l_name.title()
#     print(f_name.title())
#     print(l_name)
#
# format_name("askar","ANDELA")

# can declare with var:
def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("sulthan", "YU")

# CAN ALSO DO THIS:
def name_format(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = name_format("sulthan", "YU")
print(formated_string)
