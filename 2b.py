def binni_to_deciiii():
    binn = int(input("Enter no in binary: "))
    
    dec = 0
    i = 0
    rem1 = binn%10
    if rem1>1:
        print("invalid input")
        exit(0)
    else:       
        while (binn!=0):
            dec+=(binn%10)*(2**i)
            i+=1
            binn //= 10
        print("dec: ",dec) 

binni_to_deciiii() 

def oct_to_hex():
    oct = int(input("Enter number in oct form: "))
    dec = 0
    i = 0
    rem1 = oct%10
    if rem1>7:
        print("Not a valid input")
        exit(0)
    else:
        while oct!=0:
            dec += (oct%10)*(8**i)
            i+=1
            oct//=10
        hex=""
        while dec!=0:
            rem= dec%16
        
            if rem<10:
                hex += str(rem)
            else:
                hex += chr(ord('A') +rem - 10)
            dec//=16

        hex=hex[::-1]
        print("Hex: ",hex)


oct_to_hex()
    