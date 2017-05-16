#!user/bin/python
def rr():
	print("Round Robin Algo")
	running_queue=[]
	arrival_time=[]
	burst_time=[]
	process={}
	time_slice=input("Enter Time Slice:")
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
		process[arrival_time[index]]=[index+1,burst_time[index]]
	arrival_time.sort()
	print("Ordered according to Arrival time:")
	for index in range(0,process_num):
		print arrival_time[index],"------"
	CPU_time=min
	print("Time of processes on CPU:")
	print CPU_time, "__________"
	for index in range(0,process_num):
		running_queue.append(burst_time[index])
		CPU_time=CPU_time+time_slice
		print CPU_time,"__________"
		burst_time[index]=burst_time[index]-time_slice
		if(burst_time[index]>0):
			running_queue.append(burst_time[index])
			process_num=process_num+1
rr()
