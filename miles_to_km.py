# Miles to Kilometers  |  Kilometers to Miles  - Truzz Blogg
# Source code used in this video: https://youtu.be/T2MMqi878w4

def menu_selection():
    print(4 * "~", "CONVERT KM TO MILES | MILES TO KM", 4 * "~")
    print ("Choose a type of Conversion")
    print ("[ 1 ] Km to Miles")
    print ("[ 2 ] Miles to Km")

main_loop = True

while not main_loop == False:
    menu_selection()
    user_selection = str(input("So...What would you like to do? Enter your choice [1 or 2]: "))

    if(user_selection == "1"):
        user_in_km = int(input("Please, enter the number of KILOMETERS would you like to convert: "))
        to_miles = round(user_in_km / 1.6093, 3)
        
        print(30 * "~%")
        print("{} Km converts to {} Miles.".format(user_in_km,to_miles))
        print(30 * "%~")
        keep_converting = input("Would you like to continue converting? [ yes  |  no ]")
        if(keep_converting == "yes"):
            continue
        elif(keep_converting == "no"):
            main_loop = False
          
        else:
            print("Wrong choice! Bye Bye!")
            break  
           
        
    elif(user_selection == "2"):
        user_in_miles = int(input("Please, enter the number of MILES would you like to convert: "))
        to_kilometers = round(user_in_miles * 1.6093, 3)
        
        print(30 * "~%")
        print("{} Miles converts to {} Kilometers.".format(user_in_miles,to_kilometers))
        print(30 * "%~")
        keep_converting = input("Would you like to continue converting? [ yes  |  no ]")
        if(keep_converting == "yes"):
            continue
        elif(keep_converting == "no"):
            main_loop = False
          
        else:
            print("Wrong choice! Bye Bye!")
            break  
    

   
    
   
