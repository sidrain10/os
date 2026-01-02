n = int(input("Enter the number of processes: "))

processes = []
arrival_times = []
burst_times = []


for i in range(n):
  processes.append(f"P{i+1}")
  at = int(input(f"Enter the arrival time for P{i+1}: "))
  bt = int(input(f"Enter the burst time for P{i+1}: "))

  arrival_times.append(at)
  burst_times.append(bt)


process_data = list(zip(processes, arrival_times, burst_times, range(n)))  

start_time = [-1] * n
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

remaining_time = burst_times[:]

current_time = 0
completed = 0


while completed < n:
  ready = [p for p in process_data if (p[1] <= current_time and remaining_time[p[3]] > 0)]

  if not ready:
    not_done = [p for p in process_data if (remaining_time[p[3]] > 0)]
    next_arrival = min(p[1] for p in not_done)
    current_time = max(current_time, next_arrival)
    continue

  ready.sort(key= lambda x : (remaining_time[x[3]], x[1], x[3]))
  chosen = ready[0]
  pname, at, bt, idx = chosen

  if start_time[idx] == -1:
    start_time[idx] = current_time

  remaining_time[idx] -= 1
  current_time += 1

  if remaining_time[idx] == 0: 
    completion_time[idx] = current_time
    turnaround_time[idx] = completion_time[idx] - at
    waiting_time[idx] = turnaround_time[idx] - bt
    completed += 1

print("\nprocess\tAT\tBT\tST\tCT\tWT\tTAT")    

for i in range(n):
  print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{start_time[i]}\t{completion_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n


