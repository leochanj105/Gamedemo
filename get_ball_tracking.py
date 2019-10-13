from ball_tracking import *
import time
import multiprocessing



if __name__ == "__main__": 
	print("1")
	# creating a pipe
	parent_conn, child_conn = multiprocessing.Pipe()

	# creating new processes


	# values =  multiprocessing.Array('d', 2)
	# value = multiprocessing.Value('i')
	p1 = multiprocessing.Process(target=main_a, args=(parent_conn, ))
	p1.start()
	result = None
	while(True):
		time.sleep(0.001)
		if(child_conn.poll()):
				result =child_conn.recv()
		print(result)
    
	# running processes

    # wait until processes finish 
	p1.join() 
	
