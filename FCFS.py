#!user/bin/python
print("First Come First Serve Algo")
p={1:[0,4], 2:[2,5], 3:[5,2], 4:[6,3]}
t_time=0
b_time=0
#a_time1=[]
#b_time1=[]
#process=[]
#p_num=input("Enter total number of processes:")
#for index in range(1,p_num):
	#a_t=input("Enter arrival time:")
	#a_time1.append(a_t)
	#b_t=input("Enter burst time:")
	#b_time1.append(b_t)
	#process[index+1]=[a_time1[index],b_time1[index]]
#a_time1.sort()
#for index in range(1,p_num):
	#print a_time1[index],"------"
print("Time of processes on CPU:")
for index in range(1,5):
	print t_time, "__________"
	b_time=p.get(index)[1]
	t_time=t_time+b_time
print t_time
