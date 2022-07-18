#import packages
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

#Take input from the user and append it to list of list 
p = int(input("Enter total number of processes: "))
la=[]
for i in range (p):
    at = int(input("Enter process arrival time for process %d: " %i))
    bt = int(input("Enter process burst time for process %d : " %i))
    data=[i,at,bt]
    la.append(data)

#sorting of arrival time    
def arrival(elem):
    return elem[1]
la.sort(key=arrival)

#Calculate the Completion time and insert it to the list
completiontime = la[0][1] + la[0][2]
for i in range (len(la)):
    if i == 0:
        completiontime = la[0][1] + la[0][2]
        la[i].insert(3,completiontime)
    else:
        completiontime = completiontime + la[i][2]
        la[i].insert(3,completiontime)

#Calculate the Turn Around time and insert it to the list
for tat in range (len(la)):
    la[tat].insert(4,(la[tat][3] - la[tat][1]))
    
#Calculate the Waiting Time and insert it to the list
for wt in range (len(la)):
    la[wt].insert(5,(la[wt][4] - la[wt][2]))

#Gantt Chart data
gs=[]
for s in range (len(la)):
    if s == 0:
        st = la[0][1]
        gs.append(st)
    else:
        st = la[s][3] - la[s][2]
        gs.append(st)
gp=[row[0] for row in la]
gb=[row[2] for row in la]

#Plot the gantt chart
def gantt(Pro, b, st):
    for j in range(len(Pro)):
        i = Pro[j] - 1
        plt.barh(i, b[j],left=st[j])
gantt(gp, gb, gs)
plt.yticks(np.arange(max(gp)), np.arange(1, max(gp) + 1))
plt.title("Gantt Chart")
plt.xlabel("<-- Time -->")
plt.ylabel("<-- Process --> ")
plt.show()

#Table creation and calculation of averages
avg=np.mean(la, axis = 0)
la.insert(0,["Process","Arrival time", "Burst time","Completion time","Turn Around time","Waiting time"])
fig = ff.create_table(la)
fig.show()
print("The Average Turn Around Time of the processes is %f" %avg[4])
print("The Average Waiting Time of the processes is %f" %avg[5])