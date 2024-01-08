

name = input("Type your name :?")
print("Welcome",name,"to this adventure!")

answer = input("you are lost in a forest and you have two ways to get out and you can go  left or right.which way would you like to go?").lower()
    
if answer =="left":
    answer = input("you come to a river,you can walk around and swim to swim across:")

    if answer =="swim":
        print("you swam across and were eaten by an alligator ,")
    elif answer =="walk":
        print("you find a house and demon that lives in that house kills you````")
    else:
        print('not a valid option,you loose,')
elif answer =="right":
    answer = input("you come to a bridge it looks wobbly ,do u want to cross it or head back?(cross/back)")
    if answer =="back":
        print("you go back and loose")
    elif answer=="cross":
        answer == input("you cross the bidge and meet a stranger,do you talk to them(yes/no)?")
        if answer =="no":
             print("you ignore the stranger and they are offended and you loose")
           
        elif answer =="yes":
                print("you talk to the stranger and stranger give you car key and you rached home!!!")
        else:
            print("not a valid option,game over")

    else:
            print("not a valid option,game over")
   


else:
            print("not a valid option,game over")


            print('not a valid option,you loose,')

    

    
