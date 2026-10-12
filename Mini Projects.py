# Calculator   1st project

# a = int(input("enter 1st number: "))
# b = int(input("enter 2nd number: "))
# op = input("enter operator (+,-,*,%,/,**,//): ")

# if op == '+':
#     print(a+b)
# elif op == '-':
#     print(a-b)
# elif op == '*':
#     print(a*b)
# elif op == '%':
#     print(a%b)
# elif op == '/':
#     print(a/b)
# elif op == '**':
#     print(a ** b)
# elif op == '//':
#     print(a // b)
# else :
#     print("exit")


# # game guessing 

# import random
# def game():
#     number = random.randint(1,30)
#     while True:
#         user_number = int(input("enter number: "))
#         if user_number ==  number:
#             print("you won: ")
#             break
#         elif user_number > number:
#             print("too high: ")
#         elif user_number < number:
#             print("too low: ")
#     print("Thank you for playing: ")
# game()


# expenses tracer

# def expense():
#     n = int(input("how many expenses do you want to enter: "))
#     expenses_names = []
#     expenses_amount = []
#     total = 0
#     for i in range(n):
#         name = (input("Enter expenses name: "))
#         amount = int(input("enter amount: "))
#         expenses_names.append(name)
#         expenses_amount.append(amount)
#         total = total + amount
#     for i in range(n):
#         print(expenses_names[i],expenses_amount[i])
#         print("total amount spend: ",total)
# expense() 


# Rock paper scissors Game
import random 
def game():
    n = input("enter your choice: ")
    computer_choice = random.choice(["rock","paper","scissor"])
    print("computer_choice: ",computer_choice)
    if n == computer_choice:
        print("It's a draw")
    elif (n == "rock" and computer_choice == "paper"):
        print("you lose")
    elif (n == "paper" and computer_choice == "rock"):
        print("you win")
    elif (n == "scissor" and computer_choice == "rock"):
        print("you lose")
    elif (n == "rock" and computer_choice == "scissor"):
        print("you win")
    elif (n == "paper" and computer_choice == "scissor"):
        print("you lose")
    elif (n == "scissor" and computer_choice == "paper"):
        print("you win")
game()
