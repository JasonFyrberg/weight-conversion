#program to help powerlifters convert pounds to kg and tell them how much to load onto the bar

#check to make sure user entered a positive whole number
def is_positive_whole_number(x):
    return x.isdigit() and int(x) >= 0

def is_positive_number(x):
    return (isinstance(x, int) or isinstance(x, float)) and x >= 0


#kg to lbs conversion
def convert_lbs_to_kg(x):
    x = float(x)
    kg_conversion = round(x / 2.20462, 1)
    print(f"That is {kg_conversion} kilograms!\n")

#lbs to kg conversion 
def convert_kg_to_lbs(x):
    x = float(x)
    lbs_conversion = round(x * 2.20462, 1)
    print(f"That is {lbs_conversion} pounds!\n")
 
#calculate weight on bar lbs
def bar_weight_lbs(weight):

        #list of all possible lbs plates
        lbs_plates = [45, 35, 25, 10, 5, 2.5, 1.25]
        num_plates = [0, 0, 0, 0, 0, 0, 0]

        #calculate for one side of the bar
        load_weight = (int(weight) - 45) / 2

        for i in range(len(lbs_plates)):
            if load_weight >= lbs_plates[i]:
                num_plates[i] = int(load_weight // lbs_plates[i])
                load_weight %= lbs_plates[i]

        #print number of plates per side
        for i in range(len(lbs_plates)):
            if num_plates[i] > 0:
                print(f"{num_plates[i]} {lbs_plates[i]} pound plate(s)")

#calculate weight on bar kgs
def bar_weight_kg(weight):

    # list of all possible lbs plates
    kg_plates = [50, 25, 20, 15, 10, 5, 2.5, 2, 1.5, 1.25, 1, 0.5, 0.25]
    num_plates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # calculate for one side of the bar
    load_weight = (weight - 20) / 2

    for i in range(len(kg_plates)):
        if load_weight >= kg_plates[i]:
            num_plates[i] = int(load_weight // kg_plates[i])
            load_weight %= kg_plates[i]

    # print number of plates per side
    for i in range(len(kg_plates)):
        if num_plates[i] > 0:
            print(f"{num_plates[i]} {kg_plates[i]} kilogram plate(s)")

