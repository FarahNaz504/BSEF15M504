#!user/bin/python
def priority():
	print("Priority Algo")
	arrival_time=[]
	burst_time=[]
	priority_order=[]
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
		pri_order=input("Enter priority order:")
		priority_order.append(pri_order)
		process[priority_order[index]]=[arrival_time[index],burst_time[index],index+1]
	priority_order.sort()
	print("Ordered according to priority:")
	for index in range(0,process_num):
		print priority_order[index],"------"
	CPU_time=min
	print("Time of processes on CPU:")
	print CPU_time, "__________"
	for index in range(0,process_num):
	
		CPU_time=CPU_time+process.get(priority_order[index])[1]
		min=CPU_time
		print CPU_time, "__________P",process.get(priority_order[index])[2],"completed"
priority()

