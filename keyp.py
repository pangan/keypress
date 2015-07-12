import tty, termios, sys
import threading

global q

q =''
def getchar():
	#Returns a single character from standard input
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	
	global q
	q = ch
		
	if ch !='x':
		#print ord(ch)
		threading.Thread(target = getchar).start()
		
	
print "Press x to exit!"

threading.Thread(target = getchar).start()


while 1:
    #ch = getchar()
    if q == 'x':
    	exit(1)
    if q == chr(65):
    	print "UP"
    	q = ''
    if q == chr(66):
    	print "DOWN"
    	q = ''
    if q == chr(67):
    	print "RIGHT"
    	q = ''
    if q == chr(68):
    	print "LEFT"
    	q = ''
    
    