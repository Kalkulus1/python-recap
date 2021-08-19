def encrypt(plain,digit):
    
    
    digit = str(digit)
    newStr = []
    for i in range(len(digit)):
        
        newStr.append(plain[i]*int(digit[i]))
        
        
    if len(digit)!=len(plain):
        
        for i in range(len(digit),len(plain)):
            
            newStr.append(plain[i])
            
            

    return ''.join(newStr)
    
    




def decrypt(cipher,digit):
    
    digit = str(digit)
    newStr = []
    j = 0
    subStr= ''
    for i in digit:
        
        k = int(i)
        subStr = cipher[j:k+j]
        newStr.append(subStr[0])
        j = k+len(subStr)-1
        
    if len(digit)!= len(cipher):
        
        for i in range(j+1,len(cipher)):
            newStr.append(cipher[i])
                       
    
    print(''.join(newStr))
    
    
    

decrypt(encrypt('openly',123),123)