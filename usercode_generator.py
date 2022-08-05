from datetime import datetime

def generate_code():
    code = str(datetime.now().day) + str(datetime.now().microsecond)
    return code 




