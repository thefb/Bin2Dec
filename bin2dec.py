bin = input("Binario: ")


def checkBin(bin):
    if len(bin) < 9:
        result = True
        for x in bin:
            if int(x) > 1:
                result = False
        return result
    else :
        return "This is bigger than 8-digits."


def bin2dec(bin):
    if checkBin(bin):
        l = len(bin) - 1
        decimal = 0
        for b in bin:
            x = int(b) * (2**l)
            decimal += x
            l -= 1
        return decimal
    else:
        return "Number not allowed. This error is reported when the number is bigger than 8-digits or does not correspond to 1 and 0's."

print(bin2dec(bin))
