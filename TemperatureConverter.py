def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


Temperature = {" Celsius ": " C ", " Fahrenheit ": " F ", " Kelvin ": " K "}

def temperature_converter(temp_val, in_temp, out_temp):

    if in_temp == 'C':

        if out_temp == 'F':

            return celsius_to_fahrenheit(temp_val)

        elif out_temp == 'K':
            return celsius_to_kelvin(temp_val)
    elif in_temp == 'F':
        if out_temp == 'C':
            return fahrenheit_to_celsius(temp_val)
        elif out_temp == 'K':
            return fahrenheit_to_kelvin(temp_val)
    elif in_temp == 'K':
        if out_temp == 'C':
            return kelvin_to_celsius(temp_val)
        elif out_temp == 'F':
            return kelvin_to_fahrenheit(temp_val)
    else:
        return "Invalid input or output unit."


print("Enter the temperature value:")
temp = float(input()) 
print("Enter the input temperature unit(C, F or K)")
input_unit = input().upper()
print("Enter the output temperature unit(C, F or K)")
output_unit = input().upper()
result = temperature_converter(temp, input_unit, output_unit)
print(f"{temp}{input_unit} is {result}{output_unit}")
