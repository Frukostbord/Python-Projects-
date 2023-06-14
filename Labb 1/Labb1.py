'''
Function for converting temperatures between Fahrenheit and Celcius
'''

def fahrenheit_to_celcius(n):
    return (n - 31) * 0.5556   #Conversion of value
def celcius_to_fahrenheit(n):
    return (n * 1.8) + 32      #Conversion of value

def main():
    unit = input("What do you want to convert IN to? Write 'F' for Fahrenheit and 'C' for Celcius: ")  #Acquiring unit
    temp = input("Please write unit in numbers, e.g: '23': ") #Acquiring value
    if unit.upper() == "F" and temp.isdigit():     #Condition statement for unit and temp, ignores letter case.
        t_celcius = celcius_to_fahrenheit(float(temp))
        print(temp, "degree(s) Celcius is", t_celcius, "degree(s) Fahrenheit")
    elif unit.upper() == "C" and temp.isdigit():  #Condition statement for unit and temp, ignores letter case.
        t_fahrenheit = fahrenheit_to_celcius(float(temp))
        print(temp, "degree(s) Celcius is", t_fahrenheit, "degree(s) Fahrenheit")
    else:                                                    #If no correct input is given.
        print("Wrong value put in by user.")
main()
