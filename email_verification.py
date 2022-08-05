def checkEmailFormat(email):
    ad = 0
    dot = 0
    address = 0
    end = 0
    first = 0
    for i in range(len(email)):
        if i == 0:
            if email[i].isdigit == False:
                return False
            else:
                first+= 1
        else:
            if email[i] == '@':
                ad+= 1
                if i != len(email) - 1:
                    if email[i+1].islower() == True:
                        address+= 1
                    else:
                        return False
                else:
                    return False
            elif email[i] == '.':
                dot+= 1
                if i != len(email) - 1:
                    if email[i+1].islower() == True:
                        end+= 1
                    else:
                        return False
                else:
                    return False
    if first > 0 and dot > 0 and ad > 0 and address > 0 and end > 0:
        return True
    return False

