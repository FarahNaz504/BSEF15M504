#!user/bin/python
print("Shortest Job First Algo")
p={1:[0,1], 2:[0,3], 3:[0,4]}
b_time=0
t_time=0
#a_time1=[]
#b_time1=[]
#process=[]
#p_num=input("Enter total number of processes:")
#for index in range(1,p_num):
#	a_t=input("Enter arrival time:")
#	a_time1.append(a_t)
#	b_t=input("Enter burst time:")
#	b_time1.append(b_t)
#	process[index+1]=[a_time1[index],b_time1[index]]
#b_time1.sort()
#for index in range(1,p_num):
#	print b_time1[index],"------"
print("processes time on CPU:")
for i in range(1,4):
	print t_time,"______"
	b_time=b_time+p.get(i)[1]
	t_time=t_time+b_time
print t_time

