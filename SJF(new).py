#!user/bin/python
print("Shortest Job First Algo")
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
	p[b_time1[index]]=[a_time1[index],index+1]
b_time1.sort()
print("Ordered according to Burst time:")
for index in range(0,p_num):
	print b_time1[index],"------"
t_time=min
print("Time of processes on CPU:")
print t_time, "__________"
for index in range(0,p_num):
	
	t_time=t_time+b_time1[index]
	min=t_time
	print t_time, "__________p",p.get(b_time1[index])[1],"completed"
