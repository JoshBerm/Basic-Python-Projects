class PA1:
    length = float(input("Enter the backyard length: "))
    width = float(input("Enter the backyard width: "))

    def calculate_area(length, width):
        backyard_area = 0.0
        backyard_area = length * width
        return backyard_area
    print(f'The backyard area is: {calculate_area(length, width)}ft')
    
    tent_width = float(input("Enter the tent width: "))
    while(tent_width > width):##Checks whether the entered tent width is bigger than that of the backyard
        tent_width = float(input("The tent width is larger than the width of the backyard! Retry and enter the new width so that it can fit: "))##tent_width grabs the input as a float value
    
    tent_height = float(input("Enter the tent height: "))

    def tent_front_area(tent_width, tent_height):
        tent_from_area = 0.5 * tent_width * tent_height
        return tent_from_area
    print(f'The front area is {tent_front_area(tent_width, tent_height):.2f}')
    
    flowers = int(input('Enter how many flowers minimum: '))
    def size_flower_bed(flowers):
        while(flowers < 0):
            flowers = int(input('You can not have a negative amount of flowers in your flower bed. Please re-enter a correct amount'))
        if(flowers == 0):
            return flowers
        else:
            size_flower_bed = int(((flowers -1) ** 0.5) + 1)
            return size_flower_bed
    print(f'Each side has {size_flower_bed(flowers)} beautiful flowers ')