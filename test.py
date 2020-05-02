from termcolor import colored

cd = '\u2666'

stri = \
        '''
10%s
   %s   %s
   %s   %s
   %s   %s
   %s   %s
		%s10''' % (cd, cd, cd, cd, cd, cd, cd, cd, cd, cd)
lines = stri.split('\n')
for i in lines:
    if len(i) < 12:

        i += (12 - len(i)) * ' '
    print(colored(i, color='red', on_color='on_white'))
