class Factorial:
    
    def findFactorial(self):
        try:
            self.user_input = int(input("Please enter the number: "))
            self.user_input_copy = self.user_input
            factorial = 1
            for i in range(1,self.user_input):
                factorial = factorial*(self.user_input)
                self.user_input = self.user_input - 1

        except Exception as e:
            print(f"Error: {e} \n Please try again with valid input")
            exit()

        return factorial

f = Factorial()
fact = f.findFactorial()

ip = f.user_input_copy

print(f"factorial of {ip} is {fact}")
