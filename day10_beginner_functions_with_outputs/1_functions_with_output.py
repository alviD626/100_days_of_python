def format_name(f_name,l_name):
    # f_cap=  f_name.capitalize()
    # l_cap=  l_name.capitalize()
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"
    
f_name = input()
l_name = input()
print(format_name(f_name,l_name))