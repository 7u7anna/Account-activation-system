def checkRequirementsMeet(password):
    number_ch = 0
    capital_ch = 0
    lower_ch = 0
    if len(password) > 20:
        return False
    elif len(password) < 8:
        return False
    else:
        for i in range(len(password)):
            if password[i].isupper() == True:
                capital_ch+= 1
            elif password[i].isdigit() == True:
                number_ch+= 1
            elif password[i].islower() == True:
                lower_ch+= 1
            elif str(password[i]) == ' ':
                return False
        if capital_ch > 0 and number_ch > 0 and lower_ch > 0:
            return True
        return False

def checkPasswordStrength(password):
    special_characters = ['!', '@', '#', '$', '%', '&', '*', '+']
    conditions = []
    conditions.append(len(password))
    length = conditions[0]
    for i in range(len(password)):
        if password[i] in special_characters:
            conditions.append('special')
        elif password[i].isupper():
            conditions.append('capital')
        elif password[i].isdigit():
            conditions.append('number')
    specials = conditions.count('special')
    capitals = conditions.count('capital')
    numbers = conditions.count('number')
    if length >= 16 and length <= 20:
        if specials > 1:
            if capitals > 1:
                if numbers > 1:
                    return 'strong'
        return 'medium'
    if length >= 12 and length < 16:
        if specials >= 1:
            if capitals >= 1:
                if numbers > 1:
                    return 'medium'
        return 'weak'
    if length >= 8 and length < 12:
        return 'weak'
