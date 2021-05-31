def GetIpAddress():
    isValidIpAddress = False
    canBeValid = True


    

    while not isValidIpAddress:
        canBeValid = True
        ipInput = input("Please enter a valid IP address: ")
        splitIpAddress = ipInput.split(".")

        for octet in splitIpAddress:
            if int(octet) < 0 or int(octet) > 255:
                isValidIpAddress = False
                canBeValid = False
            else:
                isValidIpAddress = True

        if len(splitIpAddress) != 4:
            isValidIpAddress = False
        else:
            isValidIpAddress = True
    
        if not isValidIpAddress or not canBeValid:
            isValidIpAddress = False
            print("The ip address you entered is not valid")

    if isValidIpAddress and canBeValid:
        print(ipInput + " is a valid IP address")
        

        

GetIpAddress()



    