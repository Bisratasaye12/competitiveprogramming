
def wrap(string, max_width):
    t = ''
    for i in range(len(string)):
        if i != 0 and i % max_width == 0:
            t += '\n'
        t += string[i]
    return t

