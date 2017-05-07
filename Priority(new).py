#!user/bin/python
print("Priority Algo")
a_time1=[]
b_time1=[]
pr_order=[]
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
	p_order=input("Enter priority order:")
	pr_order.append(p_order)
	p[pr_order[index]]=[a_time1[index],b_time1[index],index+1]
pr_order.sort()
print("Ordered according to priority:")
for index in range(0,p_num):
	print pr_order[index],"------"
t_time=min
print("Time of processes on CPU:")
print t_time, "__________"
for index in range(0,p_num):
	
	t_time=t_time+p.get(pr_order[index])[1]
	min=t_time
	print t_time, "__________P",p.get(pr_order[index])[2],"completed"

