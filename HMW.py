h = int(input("Enter a number: "))
position = 0

if h > 0:
    while h != 0:
        position +=1
        if h & 1:
            break
        else:
            h >>= 1
else:
    print ("Error, number needs to be more than zero.")
print ("The first set bit is in position: ", position)
    

