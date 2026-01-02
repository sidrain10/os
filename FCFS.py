# FCFS CPU Scheduling with Arrival Time (User Input)

# Number of processes
n = int(input("Enter number of processes: "))

processes = []
arrival_time = []
burst_time = []

# Taking user input
for i in range(n):
    print(f"\nProcess P{i+1}:")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    
    processes.append(f"P{i+1}")
    arrival_time.append(at)
    burst_time.append(bt)

# Combine all info for sorting
process_data = list(zip(processes, arrival_time, burst_time))

# Sort processes by arrival time
process_data.sort(key=lambda x: x[1])

# Unpack sorted data
processes, arrival_time, burst_time = zip(*process_data)

start_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n

# Calculate start, waiting, completion, and turnaround times
current_time = 0

for i in range(n):
    if current_time < arrival_time[i]:
        current_time = arrival_time[i]  # CPU idle until process arrives

    start_time[i] = current_time
    waiting_time[i] = start_time[i] - arrival_time[i]
    completion_time[i] = start_time[i] + burst_time[i]
    turnaround_time[i] = completion_time[i] - arrival_time[i]

    current_time = completion_time[i]

# Print results
print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

# Averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")
