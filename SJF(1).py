#!user/bin/python
def sjf():
	print("Shortest Job First Algo")
	arrival_time=[]
	burst_time=[]
	process={}
	process_num=input("Enter total number of processes:")
	for index in range(0,process_num):
		arrival_t=input("Enter arrival time:")
		if(index==0):
			min=arrival_t
		elif(arrival_t<min):
			min=arrival_t
		arrival_time.append(arrival_t)
		burst_t=input("Enter burst time:")
		burst_time.append(burst_t)
		process[burst_time[index]]=[arrival_time[index],index+1]
	burst_time.sort()
	print("Ordered according to Burst time:")
	for index in range(0,process_num):
		print burst_time[index],"------"
	CPU_time=min
	print("Time of processes on CPU:")
	print CPU_time, "__________"
	for index in range(0,process_num):
	
		CPU_time=CPU_time+burst_time[index]
		min=CPU_time
		print CPU_time, "__________p",process.get(burst_time[index])[1],"completed"
sjf()
