def shifTo(char,pos):
    #Function to shift the character to proper position
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #create alphabet dictionary
    alphabet = dict()
    for i in range(len(alpha)):
        alphabet[i]=alpha[i]

    ordinal = ord(char)
    
    # since A = 65 and we need to shfit 13 characters forward
    shiftedOrdinal = ((ordinal + 13)% 26)+65
        
        newPos = char

        return newPos

def rot13(str):
    
    cipher =""
    shiftby=13
    counter = len(str)

    
    
         

    for i in range(counter):
        if str[i].upper() in alpha:
            cipher = cipher+shifTo(str[i],shiftby)
            print (str[i])
        else:
            print("Not in alpha")
            cipher = cipher+str[i]
 
    return cipher


# Change the inputs below to test
print(rot13("SERR PBQR PNZC"))
#print(rot13("abcd efgh ijkl"))
