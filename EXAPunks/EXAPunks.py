
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

# run the code

#value_read = input('Enter command: ')

x = 3
t = 6
value_read = 'COPY 70 X'
values = value_read.split()

if (values[0] == 'ADDI') :
    addi(values[1:])

elif (values[0] == 'SUBI') :
    subi(values[1:])

elif (values[0] == 'DIVI') :
    divi(values[1:])

elif (values[0] == 'MULI') :
    muli(values[1:])

elif (values[0] == 'COPY') :
    copy(values[1:])

print(f'X = {x}')
print(f'T = {t}')