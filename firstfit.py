nb = int(input("Enter number of memory blocks: "))
blocks = []

for i in range(nb):
    blocks.append(int(input(f"Enter size of Block {i+1}: ")))

np = int(input("\nEnter number of processes: "))
processes = []

for i in range(np):
    processes.append(int(input(f"Enter size of Process {i+1}: ")))


def first_fit(blocks, processes):
    allocated = [-1] * len(processes)
    used = [False] * len(blocks)
    wastage = 0

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if not used[j] and blocks[j] >= processes[i]:
                allocated[i] = j
                wastage += blocks[j] - processes[i]
                used[j] = True
                break

    return allocated, wastage

def next_fit(blocks, processes):
    allocated = [-1] * len(processes)
    used = [False] * len(blocks)
    wastage = 0

    n = len(blocks)
    pos = 0

    for i in range(len(processes)):
        for _ in range(n):
            if not used[pos] and blocks[pos] >= processes[i]:
                allocated[i] = pos
                wastage += blocks[pos] - processes[i]
                used[pos] = True
                pos = (pos + 1) % n
                break
            pos = (pos + 1) % n

    return allocated, wastage

def best_fit(blocks, processes):
    allocated = [-1] * len(processes)
    used = [False] * len(blocks)
    wastage = 0

    for i in range(len(processes)):
        best = -1

        for j in range(len(blocks)):
            if not used[j] and blocks[j] >= processes[i]:
                if best == -1 or blocks[j] < blocks[best]:
                    best = j

        if best != -1:
            allocated[i] = best
            wastage += blocks[best] - processes[i]
            used[best] = True

    return allocated, wastage


def worst_fit(blocks, processes):
    allocated = [-1] * len(processes)
    used = [False] * len(blocks)
    wastage = 0

    for i in range(len(processes)):
        worst = -1

        for j in range(len(blocks)):
            if not used[j] and blocks[j] >= processes[i]:
                if worst == -1 or blocks[j] > blocks[worst]:
                    worst = j

        if worst != -1:
            allocated[i] = worst
            wastage += blocks[worst] - processes[i]
            used[worst] = True

    return allocated, wastage



ff, ff_w = first_fit(blocks, processes)
nf, nf_w = next_fit(blocks, processes)
bf, bf_w = best_fit(blocks, processes)
wf, wf_w = worst_fit(blocks, processes)

print("\nProcess -> Block Allocation")
print("First Fit :", ff, "\nWastage =", ff_w)
print("Next Fit  :", nf, " Wastage =", nf_w)
print("Best Fit  :", bf, " Wastage =", bf_w)
print("Worst Fit :", wf, " Wastage =", wf_w)
