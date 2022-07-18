# importing plotly library to display the data in a tubular format.
import plotly.figure_factory as ff

# function takes the user inputs for process name,arrival time and burst time and store them in lists accordingly.

def user_input(n):
    p_list = []
    a_list = []
    b_list = []
    
    # taking user values and appending them to the above lists.
    for i in range(n):
        p = input("Enter Process_name : ")
        p_list.append(p)
        a = int(input("Enter arrival time : "))
        a_list.append(a)
        b = int(input("Enter Burst time : "))
        b_list.append(b)
    
    #combining all the three lists.
    combine_user_input = list(zip(p_list,a_list,b_list))
    
    return combine_user_input


#function to sort the process according to arrival times.

def sort_values(unsorted_list):
    length = len(unsorted_list)
    for i in range(0,length):
        for j in range(0,length-i-1):
            if(unsorted_list[j][1] > unsorted_list[j+1][1]):
                unsorted_list[j],unsorted_list[j+1] = unsorted_list[j+1],unsorted_list[j]
    return unsorted_list

# function to calculate the completion time of process.
def compute_c_time(sorted_values,p_list_copy):
    c_time = 0
    c_list = []
    for i,j,k in sorted_values:
        if(i is p_list_copy[0]):
            c_time = j+k
            c_list.append(c_time)
        else:
            c_time += k 
            c_list.append(c_time)

    return c_list


# function to calculate turnaround time of process by taking the arrival time list and completion time list as parameters.
def compute_tat(completion_and_arrival):
    tat_list = []
    for i,j in completion_and_arrival:
        tat_list.append(i-j)
    
    return tat_list

# function to calculate waiting time of process by taking turnaround time list and burst time list as parameters.
def compute_wait_time(tat_and_burst):
    wait_list = []
    for i,j in tat_and_burst:
        wait_list.append(i-j)
    
    return wait_list


# Main function from where the execution of the program strats.
if __name__ == '__main__':
    N = int(input("Enter the number of process : "))
    
    #calling a function to take the user inputs.
    user_input_list = user_input(N)
    
    #calling a function to sort the process according to arrival times.
    sorted_values = sort_values(user_input_list)
    print(sorted_values)
    
    # empty lists to copy the sorted values.
    p_list_copy = []
    a_list_copy = []
    b_list_copy = []
    
    # making a copy of process,arrival time and burst time lists.
    for i,j,k in sorted_values:
        p_list_copy.append(i)
        a_list_copy.append(j)
        b_list_copy.append(k)
    
    # calling a dunction to calculate completion time.
    completion_time = compute_c_time(sorted_values,p_list_copy)

    # combining completion and arrival time lists.
    completion_and_arrival = list(zip(completion_time,a_list_copy))

    # calling function to calculate turnaround time of process.
    turnaround_time = compute_tat(completion_and_arrival)
    
    # combining the turnaround time and burst time lists.
    tat_and_burst = list(zip(turnaround_time,b_list_copy))
    
    # calling function to calculate waiting time of process.
    waiting_time = compute_wait_time(tat_and_burst)
    
    
    #defining headings that will be used to tabulate the data.
    titles = ["Process_name","arrival_time","burst_time","completion_time","turn around_time","waiting_time"]
    
    # combining all the lists to tabulate the data.
    fcfs_list = list(zip(p_list_copy,a_list_copy,b_list_copy,completion_time,turnaround_time,waiting_time))
    fcfs_list.insert(0,titles)
    
    # creating a table using plotly library
    list_table = ff.create_table(fcfs_list)
    
    # displaying the table of data
    list_table.show()
    
    # calculation of average Turnaround Time of process.
    print("Average turnaourd time = ",sum(turnaround_time)/(len(turnaround_time)))
    
    # calculation of Averaga Waiting Time of process.
    print("Average waiting time = ",sum(waiting_time)/(len(waiting_time)))
