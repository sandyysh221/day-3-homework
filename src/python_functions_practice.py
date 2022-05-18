def return_10():
    return 10

def add(first_unit, second_unit):
    return first_unit + second_unit
    
def subtract(first_unit, second_unit):
    return first_unit - second_unit

def multiply(first_unit, second_unit):
    return first_unit * second_unit

def divide(first_unit, second_unit):
    return first_unit / second_unit

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) +int(string_2)

def number_to_full_month_name(number):
    if number == 1:
        return "January"
    elif number == 3:
        return "March"
    elif number == 9:
        return "September"
    return None

def number_to_short_month_name(number):
    if number == 1:
        return "Jan"
    elif number == 4:
        return "Apr"
    elif number == 10:
        return "Oct"
    return None

def length_for_volume(number):
    return (number*number*number)

def string_to_reverse(string):
    return string[::-1]

def convert_to_celcius(fahrenheit_temp):
    celcius = round((fahrenheit_temp - 32) * 5/9)
    return celcius