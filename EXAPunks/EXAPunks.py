
x = 0
t = 0

def addi(args) :
    total = int(args[0]) + int(args[1])

    if (args[2] =='X') :
        global x
        x = total
    elif (args[2] == 'T') :
        global t
        t = total

# run the code

#value_read = input('Enter command: ')
value_read = 'ADDI 1 2 T'
values = value_read.split()

if (values[0] == 'ADDI') :
    addi(values[1:])

print(f'X = {x}')
print(f'T = {t}')
