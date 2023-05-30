# This program uses an array of functions to determine the total area to be painted in a household
# Requests the user to input the number of rooms to be painted and the qualities of each room
# Such as 4 walls (square or rectangular) or custom walls with different values for height and length
# Any windows or doors will not be painted and are deducted from the final paintable area
# As per document, 1 gallon of paint will cover 350 square feet and costs 42 CAD
# 
# ----------------------------------------------------------------------------------------------------- #
# 
# Begin function definitions

# asks the user to input a number corresponding to the type of room to be calculated
def computeRoomArea():
    check_room = True
    while check_room:
        room_type = input('Select the shape of the room:\n1 - Rectangular\n2 - Square\n' + 
                          '3 - Custom (more or less than 4 walls, all square or rectangles)\n')
        
        # Uses string to determine which function should be executed and value returned
        # check_unit is used to determine if one of three valid inputs is used
        match room_type:
            case '1':
                check_room = False
                area_room = computeRectangleWallsArea()
            case '2':
                check_room = False
                area_room = computeSquareWallsArea()
            case '3':
                check_room = False
                area_room = computeCustomWallsArea()
            case _:
                print('Invalid input, please enter a valid number')
        
    # Obtains areas not to be painted
    area_windows_walls = computeWindowsDoorArea()
    
    return round((area_room - area_windows_walls), 1)

# asks user to input a value each for length, width and height
# then returns the value of two widths and lengths multiplied by height
def computeRectangleWallsArea():
    # check_unit is used before each input to ensure valid number input
    # if check passes, turns input into float to allow decimal inputs
    check_unit = True
    while check_unit:
        length = input('Enter the length of the room in feet:\n')
        if not length.isnumeric():
            print('Invalid input, please enter a valid number')
        else:
            check_unit = False
            length = float(length)
    
    check_unit = True
    while check_unit:
        width = input('Enter the width of the room in feet:\n')
        if not width.isnumeric():
            print('Invalid input, please enter a valid number')
        else:
            check_unit = False
            width = float(width)
    
    check_unit = True
    while check_unit:
        height = input('Enter the height of the room in feet:\n')
        if not height.isnumeric():
            print('Invalid input, please enter a valid number')
        else:
            check_unit = False
            height = float(height)
    
    # rectangular room consists of two pairs of matching walls, multiply each value by height
    return round((2*(computeRectangleArea(length, height)+computeRectangleArea(width, height))), 1)

#  simply multiplies the inputed length by the inputed width, used for windows/doors calculations
def computeRectangleArea(length, width):
    return round((length * width), 1)

# asks user to input a value each for length
# then returns the value of 4 times the square area
def computeSquareWallsArea():
    # check_unit is used before input to ensure valid number input
    # if check passes, turns input into float to allow decimal inputs
    check_unit = True
    while check_unit:
        length = input('Enter the length of the room in feet:\n')
        if not length.isnumeric():
            print('Invalid input, please enter a valid number')
        else:
            check_unit = False
            length = float(length)
    
    # square rooms consist of four matching walls, however document's function ignores height
    return round((4 * computeSquareArea(length)), 1)

#  simply multiplies the inputed length by itself, effectively squares the input
def computeSquareArea(length):
    return round((length ** 2), 1)

# asks the user how many windows/doors there are, then asks for a length and width for each iteration
# once both values are entered, mutliplies those values with each other
# and adds to a total which will be returned
def computeWindowsDoorArea():
    # check_unit is used before input to ensure valid number input
    # if check passes, turns input into integer
    check_unit = True
    while check_unit:
        amount = input('How many windows and doors does the room contain?\n')
        if not amount.isnumeric():
            print('Invalid input, please enter a valid number')
        else:
            check_unit = False
            amount = int(amount)

    windowsDoorArea = 0
    for current in range(amount):
        # check_unit is used before input to ensure valid number input
        # if check passes, turns input into float to allow decimal inputs
        check_unit = True
        while check_unit:
            length = input(f'Enter the window/door length for window/door {current+1} in feet\n')
            if not length.isnumeric():
                print('Invalid input, please enter a valid number')
            else:
                check_unit = False
                length = float(length)

        check_unit = True
        while check_unit:
            width = input(f'Enter the window/door width for window/door {current+1} in feet\n')
            if not width.isnumeric():
                print('Invalid input, please enter a valid number')
            else:
                check_unit = False
                width = float(width)
        
        windowsDoorArea += computeRectangleArea(length, width)

    return round(windowsDoorArea, 1)

# asks user to input how many walls to calculate for, then asks for height and length of wall
# once both values are entered, mutliplies those values with each other
# and adds to a total which will be returned
def computeCustomWallsArea():
    # check_unit is used before input to ensure valid number input
    # if check passes, turns input into integer
    check_unit = True
    while check_unit:
        amount = input('How many walls are there in the room?\n')
        if not amount.isnumeric():
            print('Invalid input, please enter a valid number')
        else:
            check_unit = False
            amount = int(amount)

    # custom rooms calculate the sum of wall areas, each wall having individual inputs
    roomArea = 0
    for current in range(amount):
        # check_unit is used before input to ensure valid number input
        # if check passes, turns input into float to allow decimal inputs
        check_unit = True
        while check_unit:
            height = input(f'Enter the height of wall {current+1} in feet\n')
            if not height.isnumeric():
                print('Invalid input, please enter a valid number')
            else:
                check_unit = False
                height = float(height)

        check_unit = True
        while check_unit:
            length = input(f'Enter the length of wall {current+1} in feet\n')
            if not length.isnumeric():
                print('Invalid input, please enter a valid number')
            else:
                check_unit = False
                length = float(length)
            
        roomArea += computeRectangleArea(length, height)

    # final value given once all walls are accounted for
    return roomArea

# simply returns the amount of gallons needed, rounded to second decimal
def computeGallons(area):
    gallon_room = area / gallon_per_area
    return round(gallon_room, 2)

# simply returns the cost of gallons needed, rounded to second decimal
def computePaintPrice(area):
    price_room = (area / gallon_per_area) * gallon_cost
    return round(price_room, 2)

# End function definitions
# 
# ----------------------------------------------------------------------------------------------------- #
# 
# Begin user interaction

area_total = 0
gallon_total = 0
price_total = 0
gallon_per_area = 350 # one gallon covers 350 square feet
gallon_cost = 42 # one gallon costs 42 CAD
print('Welcome to Shiny Paint Company for indoor painting!')

# check_select used for input checking
check_select = True

while check_select:
    select = input('How many Rooms do you want to paint:\n')
    # check to ensure valid number is entered, with 0 simply ending the program quickly
    if not select.isnumeric() or not (int(select) >= 0):
        print('Invalid input, please enter a valid number')
    else:
        check_select = False
        select = int(select)
        print('Thank you!')

        # run iterations for every room type, allowing different types to be calculated each time
        for current in range(select):
            print(f'Room: {current+1}')
            area_room = computeRoomArea()
            area_total += area_room
            gallon_room = computeGallons(area_room)
            gallon_total += gallon_room
            price_room = computePaintPrice(area_room)
            price_total += price_room

            # total values are used once all rooms have been accounted for
            print(f'For Room: {current+1}, the area to be painted is {area_room:.1f} square ft ' + 
                  f'and will require {gallon_room:.2f} gallons to paint. ' + 
                  f'This will cost the customer ${price_room:.2f}')
    
        print(f'Area to be painted is {area_total:.2f} square ft ' + 
              f'and will require {gallon_total:.2f} gallons to paint. ' + 
              f'This will cost the customer ${price_total:.2f}')
