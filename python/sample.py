import vim

def opened_parenthesis(line, cursor):
    found  = 0
    position = 0
    for i, letter in enumerate(reversed(line[:cursor])):
        if (letter == '('):
            found = found + 1
            position = i
        elif (letter == ')'):
            found = found - 1

    position = len(line[:cursor]) - position 
    if (found > 0):
        return True,position
    return False,0

def line_ended_in_comma(line, cursor):
    print(line, ' ', cursor)
    striped_line = line[:cursor].rstrip()
    #Remove tabs to check if the line stars with a space
    notab_line = line.replace('\t', '')
    print (striped_line[len(striped_line)-1])
    if ((striped_line[len(striped_line)-1] == ',') and notab_line[0] == ' '):
        position = len(notab_line) - len(notab_line.lstrip())
        return True,position
    else:
        return False,0

    
#TODO mantain the TAB at the beginning of the previous line
def edit_file(cb, line, colum, row, indexation_string):
    cb[row] = line[:colum].rstrip()
    cb.append(indexation_string+line[colum:].strip(),row+1)


def print_country():
    current_range = vim.current.range
    cb = vim.current.buffer
    cw = vim.current.window
    pos = cw.cursor
    row = pos[0]-1
    colum = pos[1]+1
    line = cb[row]
    ret = opened_parenthesis(line, colum)
    spaces = ""
    if (ret[0] == True):
        edit_file(cb, line, colum, row, spaces.rjust(ret[1],' '))
        vim.command('let changeIndex = 1')
    else:
        ret = line_ended_in_comma(line, colum)
        print (ret)
        if (ret[0] == True):
            edit_file(cb, line, colum, row, spaces.rjust(ret[1],' '))
            vim.command('let changeIndex = 1')
        else:
            vim.command('let changeIndex = 0')
    #print ('You seem to be in %s' % _get_country())
