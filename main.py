from weight_conversion import *

while True:
    #prompt user with options
    ask = int(input("\nWhat can I help you with?\n"
                    "1.) Convert kilograms to pounds\n"
                    "2.) Convert pounds to kilograms\n"
                    "3.) Load kilogram plates onto the bar\n"
                    "4.) Load pound plates onto the bar\n"
                    "5.) Exit\n\n"))
    
    if ask == 1:
        while True:
            kg_input = input("Enter an amount of kilograms:\n\n")
            if is_positive_whole_number(kg_input):
                convert_kg_to_lbs(kg_input)  
                break
            else:  
                print("\nPlease enter a positive number.")    

    elif ask == 2:
        while True:
            lbs_input = input("Enter an amount of pounds:\n\n")
            if is_positive_whole_number(lbs_input):
                convert_lbs_to_kg(lbs_input)  
                break
            else:  
                print("\nPlease enter a positive number.")
        
    elif ask == 3:
        while True:
            kg_weight_input = input("How much weight in kilograms are you lifting?\n\n")
            if is_positive_whole_number(kg_weight_input):
                kg_weight_input = int(kg_weight_input)
                if kg_weight_input <= 20:
                    print("That's the bar or less!")
                else:
                    kg_weight_input = int(kg_weight_input)
                    bar_weight_kg(kg_weight_input)
                break  #exit loop if valid input
            else:
                print("\nPlease enter a positive whole number with no decimals.")
        
    elif ask == 4:
        while True:
            lbs_weight_input = input("How much weight in pounds are you lifting?\n\n")
            if is_positive_whole_number(lbs_weight_input):
                lbs_weight_input = int(lbs_weight_input)
                if lbs_weight_input <= 45:
                    print("That's the bar or less!")
                else:
                    lbs_weight_input = int(lbs_weight_input)
                    bar_weight_lbs(lbs_weight_input)
                break  #exit loop if valid input
            else:
                print("\nPlease enter a positive whole number with no decimals.")
            

    elif ask == 5:
        print("See you next time!") 
        break

    else:
        print("Invalid Input")
    