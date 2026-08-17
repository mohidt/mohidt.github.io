#Name: Mohid Tahir , 624560
#Date: December 9 , 2019
#File Name: “Inventory_Tracking_Best.py”
#Description: A simple inventory program that allows for different tasks to be completed.

#Note: To fully understand indexes and why things are the way they are, see the index explanations near the bottom of my code (my_inventory list)


#This function gets an option from the user to start a task.
def get_option():
    print(" ")
    print(" ")
    print(" ")
    print("                       *")
    print("                    **   *")
    print("                 **")  
    print("              ****        ")
    print("                *")
    print("                *")    
    print("          ***********")
    print("      *******************")
    print("     *********************")
    print("  **************************")
    print(" ****************************")
    print("******************************")
    print("Tahir's Fruit Basket Inventory")
    print("******************************")
    print(" ****************************")
    print("  **************************")
    print("   ************************")
    print("     *******************")
    print("       ***************")
    print("--------------------------")
    print("Your options are: ")
    print("--------------------------")
    print("1. List current inventory")
    print("2. List product detail")
    print("3. Add new product")
    print("4. Remove product from inventory")
    print("5. Edit product")
    print("6. Receive product into stock")
    print("7. Sale of product")
    print("8. Search")
    print("9. Quit!")
    print("--------------------------")
    print(" ")
    x = True
    while x == True:
        try: #Ensures they enter a number
            option = int(input("Please choose an option: "))
            print(" ")
            if option >= 1 and option <= 9: #Ensures they enter an option between 1 and 9
                return option
                x = False
            else:
                print("Please enter a valid option! ")
                print(" ")
        except:
            print(" ")
            print("Please enter a valid option!")
            print(" ")
    #Loops until a valid option is chosen
    
#This function converts integers to strings(This is to help with formatting)
def convert_int_to_str():
    for x in range(1, len(my_inventory)): #See the index explanations
        for y in range(2,4):
            my_inventory[x][y] = str(my_inventory[x][y]) #x is the index of the main list, while y represents the sublist's index


#This function converts strings to integers(This is also to help with formatting)
def convert_str_to_int():
    for x in range(1, len(my_inventory)): #See the index explanations
        for y in range(2,4):
            my_inventory[x][y] = int(my_inventory[x][y]) #x is the index of the main list, while y represents the sublist's index



#This function formats strings and prints them. The 's' in the text represents formatting strings specifically
def current_item_print_strings(i): #See the index explanations
    convert_int_to_str()
    print('{:<15s}{:>10s}{:^14s}{:>14s}'.format(my_inventory[i][0],my_inventory[i][1],my_inventory[i][2],my_inventory[i][3])) #i represents the index of the main list
    print("-"*55)


#This function formats strings and integers and prints them. The 's' in the text represents formatting strings specifically, while the 'd' represents integers.
def current_item_print(i): #i is a parameter in this function. When the function is called, the parameter is replaced by a value.
    convert_str_to_int()
    print('{:<15s}{:>10s}{:>14s}{:>14s}'.format(my_inventory[0][0],my_inventory[0][1],my_inventory[0][2],my_inventory[0][3])) #See the index explanations
    print("-"*55)
    print('{:<15s}{:>10s}{:^14d}{:>14d}'.format(my_inventory[i][0],my_inventory[i][1],my_inventory[i][2],my_inventory[i][3])) #i represents the index of the main list


#This function asks the user what part of a row they would like to edit. This function is called later when the user picks option 5 from the menu.    
def what_to_edit():
    print("--------------------------")
    print("Your options are: ")
    print("--------------------------")
    print("1. Edit product code")
    print("2. Edit product name")
    print("3. Edit quantity")
    print("4. Edit sales number")
    print("--------------------------")
    print(" ")
    x = True
    while x == True:
        try: #Ensures they enter an integer
            edit_choice = int(input("Please choose an option: "))
            print(" ")
            if edit_choice >= 1 and edit_choice <= 4: #Ensures they enter an option between 1 and 4
                return edit_choice
                x = False
            else:
                print("Please enter a valid option! ")
                print(" ")
        except:
            print(" ")
            print("Please enter a valid option!")
            print(" ")
    #Loops until a valid option is chosen


#This function makes sure that while adding or editing a product, you don't enter something that already exists in the inventory
def no_duplicate_codes_or_names(): 
    find_product_code = []
    find_product_name = []
    for i in range(1,len(my_inventory)):
        finding_code = my_inventory[i][0] #i represents the mainlist's index
        find_product_code.append(finding_code) #Adds existing product codes to a list
        #See the index explanations
        
    for j in range(1,len(my_inventory)):
        finding_name = my_inventory[j][1] #j represents the mainlist's index
        find_product_name.append(finding_name) #Adds existing product names to a list
        #See the index explanations

    return find_product_code,find_product_name #Returns the lists to the add_new_product and edit_product functions for later use


#This function takes a product code and displays its row. The 's' in the text represents formatting strings specifically, while the 'd' represents integers   
def linear_search():
    convert_str_to_int()
    print("-"*72)
    search = input("Please enter a product code: ")
    print("-"*72)
    found = False
    x = True
    while x == True:
        for i in range(0,len(my_inventory)):
            if my_inventory[i][0] == search: 
                print(" ")
                print(" ")
                print('{:<15s}{:>10s}{:>14s}{:>14s}'.format(my_inventory[0][0],my_inventory[0][1],my_inventory[0][2],my_inventory[0][3])) #See the index explanations
                print("-"*55)
                print('{:<15s}{:>10s}{:^14d}{:>14d}'.format(my_inventory[i][0],my_inventory[i][1],my_inventory[i][2],my_inventory[i][3])) #See the index explanations
                found = True
                x = False
                return i #Returns this value (represents main list's index) as it can be used later
            
        if found == False:
            print(" ")
            print("Product code is invalid! Try again!")
            print(" ")
            search = input("Please enter a valid product code: ")
    #Loops until valid product code is entered            

#This function lists your current inventory.  The 's' in the text represents formatting strings specifically, while the 'd' represents integers
def list_inventory():
    convert_str_to_int()
    print(" ")
    print("Now listing current inventory...")
    print(" ")
    for x in range(len(my_inventory)):
            if x == 0:
              print("-"*55)
              print('{:<15s}{:>10s}{:>14s}{:>14s}'.format(my_inventory[x][0],my_inventory[x][1],my_inventory[x][2],my_inventory[x][3])) #See the index explanations
              print("-"*55)
            else:
              print('{:<15s}{:>10s}{:^14d}{:>14d}'.format(my_inventory[x][0],my_inventory[x][1],my_inventory[x][2],my_inventory[x][3])) #See the index explanations

#This function prints the row of a specific item (shows details)        
def list_product_detail():
    print("-"*72)
    print("This will find the details of the product you are searching for.")
    linear_search()

#This function adds a new product to your inventory
def add_new_product():
    product_sublist = []
    a = True
    b = True
    x = True
    y = True
    find_product_code,find_product_name = no_duplicate_codes_or_names() #Grabs the returned values from no_duplicate_codes_or_names function
    print("This is a list of items already in your inventory: ")
    list_inventory()
    print(" ")
    print("-"*72)
    print("You will now enter the details of the product you would like to add.")
    print("-"*72)

    adding_the_product_code = input("Enter a product code: ")
    while a == True:
        if adding_the_product_code not in find_product_code: #Checks if your new product code already exists in the inventory
            if len(adding_the_product_code) == 4: #Checks to see if the product code is 4 characters long
                product_sublist.append(adding_the_product_code) #Adds the new product code to the product sublist
                a = False
            else:
                print(" ")
                print("Product code not 4 digits! Try again!")
                print(" ")
                adding_the_product_code = input("Enter a new product code: ")

            
        else:
            print(" ")
            print("Product code already in inventory! Try again!")
            print(" ")
            adding_the_product_code = input("Enter a new product code: ")
         #Loops until a valid product code is inputted   
        
    adding_the_product_desc = input("Enter the name of the product: ")
    while b == True:
        if adding_the_product_desc not in find_product_name: #Checks if your new product name already exists in the inventory
            product_sublist.append(adding_the_product_desc) #Adds the new product name to the product sublist
            b = False
        else:
            print(" ")
            print("Item already in inventory! Try again!")
            print(" ")
            adding_the_product_desc = input("Enter a new product name: ")
        #Loops until a valid product name is inputted

    while x == True:
        try: #Makes sure user enters a number as their quantity
            adding_the_quantity = int(input("Enter a quantity: "))
            x = False
        except:
            print(" ")
            print("Invalid input for quantity. Try again!")
            print(" ")
         #Loops until a valid quantity is entered

            
    while y == True:
        try: #Makes sure user enters a number as their sales number
            adding_the_sales_num = int(input("Enter the amount of sales: "))
            y = False
        except:
            print(" ")
            print("Invalid input for sales amount. Try again!")
            print(" ")
        #Loops until valid sales number is entered
    product_sublist.append(adding_the_quantity) #Adds the new quantity to the product sublist
    product_sublist.append(adding_the_sales_num) #Adds the new sales number to the product sublist
    my_inventory.append(product_sublist)
    print(" ")
    print("This is what you added:")
    print(" ")
    current_item_print(-1) #Gives -1 as the parameter to current item print. This displays the last thing added to the main list.    
    list_inventory() #Lists inventory with the new addition the the inventory


#This function deletes a product given a product code
def remove_product():
    print("-"*72)
    print("This will remove the product you wish to remove.")
    deleted_product_i = linear_search() #Grabs the returned value from linear_search function
    del(my_inventory[deleted_product_i]) #Uses that index to delete the given item and its whole row
    #See the index explanations
    list_inventory() #Lists the inventory (item is no longer there)
            

#This function edits a product given the product code
def edit_product():
    same_product_code,same_product_name = no_duplicate_codes_or_names()
    a = True
    b = True
    x = True
    y = True
    print("-"*72)
    print("This will let you edit a product of your choice.")
    print("Just enter the product code of what you'd like to edit: ")
    edit_product_i = linear_search() #Grabs the returned value from linear_search function
    print(" ")
    print("Make your edits to this product.")
    print(" ")
    final_edit_choice = what_to_edit() #Grabs the returned value from what_to_edit function

    if final_edit_choice == 1: #Runs if your choice was 1
        my_inventory[edit_product_i][0] = input("Enter the new product code: ") #Replaces existing product code with new product code
        #See the index explanations
        while a == True:
            if my_inventory[edit_product_i][0] not in same_product_code: #Checks if your edited product code already exists in the inventory
                if len(my_inventory[edit_product_i][0]) == 4: #Checks to see if the product code is 4 characters long
                    a = False
                else:
                    print(" ")
                    print("Product code not 4 digits! Try again!")
                    print(" ")
                    my_inventory[edit_product_i][0] = input("Enter a new product code: ") #Replaces existing product code with new product code 

            
            else:
                print(" ")
                print("Product code already in inventory! Try again!")
                print(" ")
                my_inventory[edit_product_i][0] = input("Enter a new product code: ") #Replaces existing product code with new product code
            #Loops until valid product code is entered

    elif final_edit_choice == 2: #Runs if choice was 2
        my_inventory[edit_product_i][1] = input("Enter the new product name: ") #Replaces existing product code with new product name
        #See the index explanations
        while b == True:
            if my_inventory[edit_product_i][1] not in same_product_name: #Checks if your edited product code already exists in the inventory
                b = False

            else:
                print(" ")
                print("Item already in inventory! Try again!")
                print(" ")
                my_inventory[edit_product_i][1] = input("Enter a new product name: ") #Replaces existing product code with new product code
            #Loops until valid product code is entered

    elif final_edit_choice == 3: #Runs if choice was 3
        while x == True:
            try: #Ensures that a number is entered for the quantity
                my_inventory[edit_product_i][2] = int(input("Enter the new quantity: "))
                #See the index explanations
                x = False
            except:
                print(" ")
                print("Invalid input for quantity. Try again!")
                print(" ")
        #Loops until valid quantity is entered

    elif final_edit_choice == 4: #Runs if choice was 4
        while y == True:
            try: #Ensures that a number is entered for the sales number
                my_inventory[edit_product_i][3] = int(input("Enter the new sales number: "))
                #See the index explanations
                y = False
            except:
                print(" ")
                print("Invalid input for sales number. Try again!")
                print(" ")
        #Loops until valid sales number is entered
    print(" ")
    print("This is the item after the edits are made: ")
    print(" ")
    current_item_print(edit_product_i) #Prints the new edited product
    list_inventory() #Lists the inventory with the edits made


#This functions updates the quantity of a specific product 
def receive_bulk():
    x = True
    print("-"*72)
    print("This will update your stock: ")
    new_stock_i = linear_search() #Grabs returned value from linear_search function
    while x == True:
        try: #Ensures the user enters a number as their quantity
            print(" ")
            updated_quantity = int(input("Enter the amount of product you received into stock: "))
            x = False
        except:
            print(" ")
            print("Please enter a valid number.")
        #Loops until valid quantity is entered
            
    my_inventory[new_stock_i][2] += updated_quantity #Adds the amount of quantity recieved to the existing quantity
    #See the index explanations
    print(" ")
    print("The stock has been updated.")
    print(" ")
    current_item_print(new_stock_i) #Sends parameter to current_item_print function in order to print the item with its updated stock
    #See the index explanations
    list_inventory() #Lists the inventory with the updated stock
            

#This function updates the amount of sales of a specific product        
def sale_of_product():
    print("-"*72)
    print("This will update your sales number: ")
    sales_num_i = linear_search() #Grabs returned value from linear_search function
    #See the index explanations
    x = True
    while x == True:
        try:  #Ensures the user enters a number as their sales number
            print(" ")
            updated_sales_num = int(input("Enter the amount sold: "))
            x = False
        except:
            print("Please enter a valid number")
        #Loops until valid sales number is entered
            
    my_inventory[sales_num_i][3] += updated_sales_num #Adds the amount of sales made to the existing quantity
    my_inventory[sales_num_i][2] -= updated_sales_num #Subtracts those sales from the quantity
    #See the index explanations
    print(" ")
    print("The sales number has been updated.")
    print(" ")
    current_item_print(sales_num_i) #Sends parameter to current_item_print function in order to print the item with its updated sales number
    list_inventory() #Lists the inventory with the updated sales number
            
#This function searches for a product once information about it is entered (letters, numbers)
def search(what_you_are_looking_for):
    found = False
    previous_x = -1 #The first time, x will not be the same same as -1
    convert_int_to_str() #Integers must be strings in order to be searched for
    for x in range(1 , len(my_inventory)): #Cycles through indexes of main list and sublist to search
        for y in range(len(my_inventory[x])):
            if what_you_are_looking_for in my_inventory[x][y]: #See the index explanations
                if x != previous_x:
                    print(" ")
                    print(what_you_are_looking_for, "appeared here:")
                    print(" ")
                    current_item_print_strings(x) #Sends parameter to current_item_print_strings function in order to print the findings
                    previous_x = x #Ebsures that if multiple of the same search text are found in the same item's information , it doesn't display more than once
                    found = True
    if found == False: #If nothing is found, this will run
        print("Not found...")
                

#This is my_inventory which is one big list, which contains sublists
#This is what each index means:
#my_inventory[0] would be the first index in the main list. That contains the product code, product, quantity, and sales number
#my_inventory{x] would be any sub list when you replace the value for x. Example: my_inventory[1] would contain BA30, Bananas, 300, 0
#my_inventory[x][0] would be any sublists first item. Example my_inventory[1][0] would be BA30
#my_inventory[x][1] would be any sublists second item. Example my_inventory[1][1] would be Bananas
#my_inventory[x][2] would be any sublists third item. Example my_inventory[1][2] would be 300
#my_inventory[x][3] would be any sublists fourth item. Example my_inventory[1][3] would be 0

my_inventory = [["Product Code:" ,"Product:", "Quantity:" , "Sales:"],
                ["BA30", "Bananas", 300,0],
                ["AP25","Apples", 200,5],
                ["MA21","Mangoes", 250,10],
                ["PE51","Peaches",50,10],
                ["TO14","Tomatoes",100,40]]

quit_program = False

list_inventory() #Lists the inventory. Inventory is listed again evertime it may be useful in a specific option
while quit_program == False:
    final_choice = get_option() #Grabs returned value from get_option function

    if final_choice == 1: #Displays the inventory(if option 1 is chosen)
        list_inventory()

    elif final_choice == 2: #Displays a specific product's details (if option 2 is chosen)
        list_inventory()
        list_product_detail()

    elif final_choice == 3: #Lets the user add a new product to the inventory (if option 3 is chosen)
        add_new_product()

    elif final_choice == 4: #Lets the user remove a specific product and all its details (if option 4 is chosen)
        list_inventory()
        remove_product()

    elif final_choice == 5: #Lets the user edit a product's details (if option 5 is chosen
        editing_loop = True
        list_inventory()
        print(" ")
        edit_product() 
        while editing_loop == True:
            print(" ")
            edit_again = input("Would you like to edit something else (Yes or No)? ")
            if edit_again == "Yes" or edit_again == "yes" :
                edit_product()
            else:
                editing_loop = False
            #Loops until the user doesn't want to edit anything else

    elif final_choice == 6: #Lets the user update their quantity of an item in stock (if option 6 is chosen)
        list_inventory()
        receive_bulk()

    elif final_choice == 7: #Lets the user say how much of an item has sold(if option 7 is chosen)
        list_inventory()
        sale_of_product()

    elif final_choice == 8: #Searches for an item given any information (if option 8 is chosen). Example: finds where the letter T has appeared
        print("-"*72)
        what_you_are_looking_for = input("Please enter what you are looking for: ")
        print("-"*72)
        search(what_you_are_looking_for) #Sends parameter to search function

    elif final_choice == 9: #Quits the program(if option 9 is chosen)
        print("-"*18)
        print("See you next time!")
        print("-"*18)
        quit_program = True
    #Loops until user decides to quit(option 9)
