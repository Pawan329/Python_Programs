'''
Write a python program which will keep adding number inputted by user and end the program once "q" is pressed.
'''

class Shopkeeper:
    
    def calculateTotalBill(self):
        try:
            total = 0
            while True:
                user_input = input("Enter the price of item else press 'q' to quit: ")
                if user_input == "q":
                    break

                elif user_input.is_interger() == False:
                    raise Exception

                else:
                    user_input = int(user_input)
                    total = total + user_input

            return total

        except Exception as e:
            print(f"Please provide a valid input. \nError code {e}")

shopkeeper = Shopkeeper()

totalBill = shopkeeper.calculateTotalBill()


print(f"Total Bill of purchased items are: Rs.{totalBill}")