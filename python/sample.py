import vim

def opened_parenthesis(line, cursor):
    found  = 0
    position = 0
    print('B Cursor', line[:cursor])
    print('A Cursor', line[cursor:])
    for i, letter in enumerate(reversed(line[:cursor])):
        if (letter == '('):
            found = found + 1
            position = i
        elif (letter == ')'):
            found = found - 1

    position = len(line[:cursor]) - position 
    print (found, position, line[position])
    if (found > 0):
        return True,position
    return False,0
    


def print_country():
    current_range = vim.current.range
    cb = vim.current.buffer
    cw = vim.current.window
    pos = cw.cursor
    row = pos[0]-1
    colum = pos[1]+1
    line = cb[row]
    ret = opened_parenthesis(line, colum)
    print (ret)
    spaces = ""
    if (ret[0] == True):
        cb[row] = line[:colum]
        cb.append(spaces.rjust(ret[1],'-')+line[colum:].strip(),row+1)
        vim.command('let changeIndex = 1')
    else:
        vim.command('let changeIndex = 0')
    #print ('You seem to be in %s' % _get_country())
