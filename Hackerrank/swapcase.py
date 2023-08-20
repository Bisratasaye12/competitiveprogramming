def swap_case(s):
    t = ''
    for i in s:
        if i.isalpha() and i.islower():
            t += i.upper()
        elif i.isalpha() and i.isupper():
            t += i.lower()
        else:
            t += i
    return t

