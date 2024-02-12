
num = int(input("Enter the number:"))
while True:
    char = input("Enter the character:")

    def coversion(num,char):
        ordinate = ord(char)
        sum = num + ordinate
        print(chr(sum))
        
        
    coversion(num,char)
    
    choice = input("Would you like to exit(y/n):")
    if(choice == 'y'):
        break
    
    else:
        pass
    
    print()
    
    
