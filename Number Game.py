import random

target=random.randint(1,100)

while True:
    userChoise=int(input("Guss the target or quite (Q): "))
    if(userChoise=="Q"):
        break

    userChoise=int(userChoise)
    if(userChoise==target):
        print("Success:Correct Guess!!")
        break
    elif(userChoise < target):
        print("your number was too small..Take a bigger guess...")
    else:
         print("your number was too big..Take a small guess...")


print("-----Game Over-----")