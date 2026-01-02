n = int(input("Enter number of processes: "))

processes = []
arrival_time = []
burst_time = []
priority = []

for i in range(n):
    processes.append(f"P{i+1}")
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority for P{i+1} (lower number = higher priority): "))

    arrival_time.append(at)
    burst_time.append(bt)
    priority.append(pr)

process_data = list(zip(processes, arrival_time, burst_time, priority, range(n)))

remaining_time = burst_time[:]
start_time = [-1] * n
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

current_time = 0
completed = 0

while completed < n:
    ready = [p for p in process_data if p[1] <= current_time and remaining_time[p[4]] > 0]

    if not ready:
        current_time += 1
        continue

    ready.sort(key=lambda x: (x[3], x[1], x[4]))
    pname, at, bt, pr, idx = ready[0]

    if start_time[idx] == -1:
        start_time[idx] = current_time

    remaining_time[idx] -= 1
    current_time += 1

    if remaining_time[idx] == 0:
        completion_time[idx] = current_time
        turnaround_time[idx] = completion_time[idx] - at
        waiting_time[idx] = turnaround_time[idx] - bt
        completed += 1

print("\nProcess\tAT\tBT\tPR\tST\tCT\tWT\tTAT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t"
          f"{start_time[i]}\t{completion_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time = {sum(waiting_time)/n:.2f}")
print(f"Average Turnaround Time = {sum(turnaround_time)/n:.2f}")
