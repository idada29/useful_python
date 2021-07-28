# Write a function that askes user for menu
menu = ['Tuna Mayo','Sausage','Bacon','British Rail','Cheese and Pickle','Chip Butty',
        'Corned Beef','Donner Kebab','Fish Finger','Shawarma','Bacon cheese','Tuna Sweetcorn',
        'Chicken Sandwich','Chilli Chicken','Chilli Onion','Indomie']


def write_file(filename):
    '''A function that writes a menu into a txt file'''
    global menu
    with open(filename,mode="w") as my_file:
        for sandwich_type in menu:
            my_file.write(sandwich_type + "\n")
# Note that the file name is the file pathl
write_file("C:/Users/dadai/Desktop/menu2.txt")

menu_output = []
def read_menu():
    '''A function to read in the menu text file'''
    global menu_output
    with open("C:/Users/dadai/Desktop/menu.txt",mode='r') as my_file:
        for line in my_file:
            menu_output.append(line.rstrip('\n'))
read_menu()

print (menu_output)
order = (input("Enter your sandwich order: ")).capitalize()

def ask_menu():
    ''' A function to ask the customers for their order choice'''
    global menu_output
    global order
    food_with_similar_ingredients = [food for food in menu_output if order in food]
    print(food_with_similar_ingredients)
    #return food_with_similar_ingredients
    if len(food_with_similar_ingredients) == 0:
        print ('Your order is not available')
    else:
        print(f'The following: {food_with_similar_ingredients} is available')   
ask_menu()

