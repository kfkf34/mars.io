from random import randint
num = randint(0,50)
scorce= True 
amount_of_quess=0
while scorce ==True:
    quest = int (input("Guest a number for 1 to 50 "))
    print (quest)
    amount_of_quess+=1
    if num == quest:
        print ("your answer was rigth")
    else:
        print ("your answer was wrong")
    if quest <=num:
        print("your quest was to low")
    elif quest >= num:
        print("your quest wae to high")
    print ("you have quess " + str (amount_of_quess)+ " of times")

