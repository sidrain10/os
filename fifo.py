n = int(input("Enter number of pages: "))
pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
faults = 0

for page in pages:
    if page not in memory:
        faults += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            memory.pop(0)  
            memory.append(page)

    print("Memory:", memory)

print("Total Page Faults:", faults)
hit = (n - faults) 
print(f"Hit Ratio: {hit/n}")