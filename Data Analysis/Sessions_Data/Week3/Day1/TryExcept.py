#Exceptions

#Python will stop your program as soon as it encounters an error.

print('Hello World')
print('Juliana')

#Try & Except Block

while True:
    try: 
        move = float(input('Give your move from 1 - 9: '))
        move = round(move)
        if move < 1 or move > 9:
            raise Exception('Choose a number within range 1-9.')
    
    except Exception as e:
        print(e)
        continue
    #finally will happen -no matter what- after any input.
    finally:
        print('finally message')

