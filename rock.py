import random
# function that contains game
def play():

    choosed_no = int(input("type 0 for Rock, 1 for paper or 2 for scissor :"))

    list = ["rock","paper","scissor"]
    choosed_item = list[choosed_no]

# here computer randomly chooses item
    computer_item = random.choice(list)
    print("computer choosed :",computer_item)

# By general rules of game finding who wins
    if choosed_item == "paper":
        if computer_item == "rock":
            print("you won")
        elif computer_item == "scissor":
            print("you lose")  
        else:
            print("draw")      


    if choosed_item == "scissor":
        if computer_item == "paper":
            print("you win")
        elif computer_item == "rock":
            print("you lose")    
        else:
            print("draw") 


    if choosed_item == "rock":
        if computer_item == "paper":
            print("you lose") 
        elif computer_item == "scissor":
            print("you win")         
        else:
            print("draw")      


# asking if user wants to play again or not             
    ask = input("do you want to play again 'yes' or 'no':")
    if ask == "yes":
        play() # calling the game function
    else:
        print("bye bye")    # ending the game


# calling the function for first time        
play()







