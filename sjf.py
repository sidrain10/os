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

done = [False] * n
start_time = [0] * n
waiting_time = [0] * n
completion_time = [0] * n
turnaround_time = [0] * n

current_time = 0
completed = 0


while completed < n:
  ready = [p for p in process_data if (p[1] <= current_time and not done[p[3]])]

  if not ready:
    next_arrival = min(p[1] for p in process_data if not done[p[3]])
    current_time = max(current_time, next_arrival)
    continue
  
  ready.sort(key = lambda x : [x[2], x[1], x[3]])
  chosen = ready[0]
  pname, at, bt, idx = chosen

  start_time[idx] = current_time
  completion_time[idx] =  start_time[idx] + bt
  waiting_time[idx] = start_time[idx] - at 
  turnaround_time[idx] = completion_time[idx] - at

  current_time = completion_time[idx]
  done[idx] = True
  completed += 1


print("\nProcess\tAT\tBT\tST\tCT\tWT\tTAT")
for i in range(n):
  print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{start_time[i]}\t{completion_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

avg_wt = sum(waiting_time) / n 
avg_tat = sum(turnaround_time) / n 

print(f"Average Waiting Time: {avg_wt:.2f}")
print(f"average turnaround Time: {avg_tat:.2f}")



