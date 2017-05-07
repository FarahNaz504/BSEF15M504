#!user/bin/python
print("First Come First Serve Algo")
a_time1=[]
b_time1=[]
p={}
p_num=input("Enter total number of processes:")
for index in range(0,p_num):
	a_t=input("Enter arrival time:")
	if(index==0):
		min=a_t
	elif(a_t<min):
		min=a_t
	a_time1.append(a_t)
	b_t=input("Enter burst time:")
	b_time1.append(b_t)
	p[a_time1[index]]=[index+1,b_time1[index]]
a_time1.sort()
print("Ordered according to Arrival time:")
for index in range(0,p_num):
	print a_time1[index],"------"
t_time=min
print("Time of processes on CPU:")
print t_time, "__________"
for index in range(0,p_num):
	t_time=t_time+p.get(a_time1[index])[1]
	min=t_time
	print t_time,"__________p",p.get(a_time1[index])[0],"completed"
