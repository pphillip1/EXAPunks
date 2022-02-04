
x = 0
t = 0

def addi(args) :
    answer = int(args[0]) + int(args[1])

    if (args[2] =='X') :
        global x
        x = answer
    elif (args[2] == 'T') :
        global t
        t = answer

def subi(args) :
    answer = int(args[0]) - int(args[1])

    if (args[2] =='X') :
        global x
        x = answer
    elif (args[2] == 'T') :
        global t
        t = answer

def muli(args) :
    answer = int(args[0]) * int(args[1])

    if (args[2] =='X') :
        global x
        x = answer
    elif (args[2] == 'T') :
        global t
        t = answer

def divi(args) :
    answer = int(args[0]) / int(args[1])

    if (args[2] =='X') :
        global x
        x = answer
    elif (args[2] == 'T') :
        global t
        t = answer

def copy(args) : 
    # if register -> register T X
    # if number -> register
    global t
    global x
        
    # look at args[0]
    if args[0] == 'T' :
        source = t
    elif args[0] == 'X' :
        source = x
    else :
        source = args[0] 
    
    # look at args[1]
    if args[1] == 'T' :
      t = source
    elif args[1] == 'X' :
      x = source

def modi(args) : 
    # if register -> register T X
    # if number -> register
    global t
    global x
        
    # look at args[0]
    if args[0] == 'T' :
        mod_source_1 = t
    elif args[0] == 'X' :
        mod_source_1 = x
    else :
        mod_source_1 = args[0] 
    
    # look at args[1]
    if args[1] == 'T' :
        mod_source_2 = t
    elif args[1] == 'X' :
        mod_source_2 = x
    else :
        mod_source_2 = args[1]
    
    if args[2] == 'T' :
      t = int(mod_source_1) % int(mod_source_2)
    elif args[2] == 'X' :
      x = int(mod_source_1) % int(mod_source_2)
# run the code

if __name__ == '__main__' :
    value_read = input('Enter command: ')

    #x = 22
    #t = 6
    #value_read = 'MODI X 7 T'
    values = value_read.split()

    if (values[0] == 'ADDI') :
        addi(values[1:])

    elif (values[0] == 'SUBI') :
        subi(values[1:])

    elif (values[0] == 'DIVI') :
        divi(values[1:])

    elif (values[0] == 'MULI') :
        muli(values[1:])

    elif (values[0] == 'DIVI') :
        divi(values[1:])

    elif (values[0] == 'MODI') :
        modi(values[1:])

    print(f'X = {x}')
    print(f'T = {t}')