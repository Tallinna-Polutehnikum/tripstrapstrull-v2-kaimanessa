
def victorycheck(sl):
    if sl[0] == sl[3] and sl[0] == sl[6]:
        return True
    elif sl[1] == sl[4] and sl[1] == sl[7]:
        return True
    elif sl[2] == sl[5] and sl[2] == sl[8]:
        return True
    elif sl[0] == sl[1] and sl[0] == sl[2]:
        return True
    elif sl[3] == sl[4] and sl[3] == sl[5]:
        return True
    elif sl[6] == sl[7] and sl[6] == sl[8]:
        return True
    elif sl[0] == sl[4] and sl[0] == sl[8]:
        return True
    elif sl[2] == sl[4] and sl[2] == sl[6]:
        return True
    
def xplays(sl):
    while True:

        location = int(input("Kuhu soovite mängida?"))
        
        if sl[location] == "x" or sl[location] == "o":
            print("See koht on täidetud!")
        else:
            slots[location] = "x"
            field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "
            print(field)
            break


def oplays(sl):
    while True:

        location = int(input("Kuhu soovite mängida?"))
        
        if sl[location] == "x" or sl[location] == "o":
            print("See koht on täidetud!")
        else:
            slots[location] = "o"
            field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "
            print(field)
            break

i = 0
slots = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "

while i != 9:
    i = i + 1
    xplays(slots)
    if victorycheck(slots) == True:
        print("X Võitis")
        break
    
    oplays(slots)
    if victorycheck(slots) == True:
        print("O Võitis")
        break
    
