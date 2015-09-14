print ("Hello world!")

i = 0

for i in range(0, 100):
    try:
        new_input = float(input())
    except ValueError:
        print ("That wasn't a number, idiot.")
        continue
    
    if ( new_input < 999.99 and new_input > -999.99 ):
        print (new_input)
    elif ( new_input < 9999.99 and new_input > -9999.99 ):
        print (new_input / 2)
    else:
        print ("Pleze gib mone plox")
        break




file = open ("tempName", "r+")

while true:
    output = file.readline()
    print (output)
    
    
file.close()
