while True:
 x = raw_input('Enter a number between 1 and 60\n> ')
 try: 
  x = int(x)
 except: print 'Nope'
 if 1 <= x <= 60: 
   print 'True'
 else: 
   print 'Fuck you buddy'

