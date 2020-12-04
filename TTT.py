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
    
def plays(sl,xo):

    while True:

        location = int(input("Kuhu soovite mängida?"))
        if sl[location] == "x" or sl[location] == "o":
            print("See koht on täidetud!")
        else:
            if xo == True:
                return "x", location
            elif xo == False: 
                return "o", location
        

i = 0
slots = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "
x_or_o = False

for i in range(9):
    x_or_o = True
    slots[plays(slots, x_or_o)[1]] = plays(slots, x_or_o)[0]
    field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "
    print(field)
    if victorycheck == True:
        print("x võitis")
    
    x_or_o = False
    slots[plays(slots, x_or_o)[1]] = plays(slots, x_or_o)[0]
    field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "
    print(field)
    if victorycheck == True:
        print("o võitis")
    
# x ja o mängijad viia ühele funktsioonile
# break konstruktsioon asendada return andmetüüp (loobume globlaasetest muutujatest, kui see pole vajalik)
