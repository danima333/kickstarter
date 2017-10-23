print('Welcome to the truth teller!')

dani = 'Daniella'

name = raw_input('Enter your name:')

if len(name) > 0 and name.isalpha():
        new_word = "%s is prettier than %s" % (dani, name) 
        print (new_word)
else:
        print ('empty')

