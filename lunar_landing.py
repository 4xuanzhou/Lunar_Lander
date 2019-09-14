Inputs that lead to a "win":0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0
Inputs that lead to a "loss":0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'''

#to ask the player if they want to play again at the end of the game
PlayAgain = True 

while PlayAgain == True:
    altitude = 100.0
    velocity = 0.0
    fuel = 100.0
    second = 0.0

    print("Welcome!")
    while altitude > 0.0:
        altitude = round(altitude,2)
        velocity = round(velocity,2)
        fuel = round(fuel,2)
        
        print("current altitude=", altitude)
        print("current fuel=", fuel)
        print("current velocity=", velocity)
        print(second, "seconds has passed.")
        burn = input("Please specify the amount of fuel you want to burn:")

        try:
            burn = round(float(burn),2)

            if burn<=fuel and burn>=0.0:
                fuel = fuel - burn
                second += 1.0
                velocity = 1.6 - burn*0.15 + velocity
                altitude = altitude - velocity

                if altitude<=0.0 and velocity >=10.0: 
                    print("Sorry! Unsafe landing at velocity =", velocity, "m/s.")
                    print("The landing took", second, "seconds.")
                    print(fuel, "liters of fuel is left.")

                if altitude<=0.0 and velocity <10.0:                    
                    print("Congratulations! Safe landing at velocity =", velocity, "m/s.")
                    print("The landing took", second, "seconds.")
                    print(fuel, "liters of fuel is left.")
#If a player tries to burn a negative amount of fuel, treat it as if they burnt zero fuel
            if burn<0.0:  
                burn=0.0
#If a player specifies to burn more fuel than they have, burn all their fuel   
            if burn>fuel:  
                burn=fuel
#to remind the player that they need to enter a valid number to specify the amount of fuel they want to burn
        except ValueError: 
            print("Please try again with a number.")  
#to ask the player again if the response begins with any other character
    AskAgain = True  

    while AskAgain == True:
        answer = input("Would you like to play again? Please enter 'Y' or 'N'.")
#Any response that begins with 'N' or 'n' will end the game        
        if answer[0] == 'N' or answer[0] == 'n':  
            PlayAgain = False
            AskAgain = False
#Any response that begins with 'Y' or 'y' will start the game again
        if answer[0] == 'Y' or answer[0] == 'y':
            PlayAgain = True  
            AskAgain = False
