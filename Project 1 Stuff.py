# Project 1 Stuff

while True:
    conversion_choice = input("Choose your conversion: \n1 for Fahrenheit to Celsius\n2 for Celsius to Fahrenheit\n3 for pounds to kilos\n4 for kilos to pounds\n5 for miles to lightyears\n6 for lightyears to miles\n0 for quit: ")
    if conversion_choice == "1":
        temp = float(input("Enter the temperature in Fahrenheit: "))
        converted_temp = (temp - 32) * 5/9
        print(f"{temp} Degrees Fahrenheit is {converted_temp:.2f} degrees Celsius.")
    elif conversion_choice  == "2":
        temp = float(input("Enter the temperature in Celsius: "))
        converted_temp = (temp * 9/5) + 32
        print(f"{temp} degrees Celsius is {converted_temp:.2f} degrees Fahrenheit.")
    elif conversion_choice == "3":
        weight = float(input("Enter the weight in pounds: "))
        converted_weight = weight * 0.453592
        print(f"{weight} pounds is {converted_weight:.2f} kilos.")
    elif conversion_choice == "4":  
        weight = float(input("Enter the weight in kilos: "))
        converted_weight = weight / 0.453592
        print(f"{weight} kilos is {converted_weight:.2f} pounds.")
    elif conversion_choice == "5":
        distance = float(input("Enter the distance in miles: "))
        converted_distance = distance / 5.878625e+12
        print(f"{distance} miles is {converted_distance:.2e} lightyears.")
    elif conversion_choice == "6":
        distance = float(input("Enter the distance in lightyears: "))
        converted_distance = distance * 5.878625e+12
        print(f"{distance} lightyears is {converted_distance:.2e} miles.")
    elif conversion_choice == "0":
        print("Goodbye!")
        break

