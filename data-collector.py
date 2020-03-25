def newJob():
    print('Starting new job. First, we need to collect some information.')
    orderNum = input('Enter Order # ')
    productNum = input('Enter product # ')
    orderQty = input('Enter quantity ordered # ')
    stockOD = input('Enter stock OD: ')
    stockID = input('Enter stock ID: ')
    material = input('Enter material: ')
    stockQty = input('Enter total stock quantity: ')

    currentQty = 0

    jobRunning = True
    while jobRunning:
        print('*** JOB STATUS ***')
        print('Order quantity: ' + currentQty +'/'+ orderQty )
        # print more info here

        print('''What do you want to do?
        1) Add good parts
        2) Add scrap parts
        3) Add raw material
        4) Save & exit''')

        runSelection = int(input('Enter an option > '))
        if runSelection == 1:
            input('How many parts? ')
        elif runSelection == 2:
            input('How many scrap?')
            input('enter scrap code: ')
        elif runSelection == 3:
            input('enter quantity of material to add: ')
        elif runSelection == 4:
            break
        else:
            print('Enter a selection 1-4')

print('''
SES job data collection. Please choose from the following options:

1) Start a new job
2) Continue from last saved job
3) Quit''')

initialSelection = int(input('Enter an option > '))
if initialSelection == 1:
    newJob()
else:
    print('That function is not enabled yet.')
