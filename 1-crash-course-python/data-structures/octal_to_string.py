def octal_to_string(octal):
    result = ""
    if not is_valid_octal(octal):
        return "Invalid Octal Passed: {}!".format(octal)
    permissions = [(4,'r'),(2,'w'), (1,'x')]
    for entity in [ int(digit) for digit in str(octal) ]:
        for num, perm in permissions:
            if entity >= num:
                result += perm
                entity -= num
            else:
                result += '-'
    return result

def is_valid_octal(octal):
    if len(str(octal)) == 3:
        for permission in str(octal):
            if int(permission) > 7:
                return False
        return True

print(octal_to_string(1000))
