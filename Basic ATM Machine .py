print("Welcome To Islamic Bank")
Trials = 3
UserPin=1234


while Trials != 0:
    Pin =int(input("Please Enter Your 4 digit Pin Number: " ))
    if Pin != UserPin:
        Trials -= 1
        print("Wrong pin Number, You Have", Trials, "Trails Left ")
    else:
        UserChoice = input("d: Deposite or w: Withdraw: ") 
        if UserChoice == "d":
            UserDeposite = input("Enter The Amount You Would Like to Deposite: ") 
            print(UserDeposite,"Pkr Have Been Deposited Into Your Account") 
        if UserChoice == "w":
            UserWithdraw = input("Enter The Amount You Would Like to Withdraw: ") 
            print(UserWithdraw,"Pkr Have Been Withdrawn From Your Account")  
    UserExit = input ("Would You Like To Continue? Y/N: ") 
    if UserExit == "N":
        print("Thank You For Using Islamic Bank") 
        break
    else:
        continue        
