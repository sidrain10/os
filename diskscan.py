n = int(input("Enter the number of disk requests: "))

requests = []
for i in range(n): 
  req = int(input(f"Enter the request {i+1}: "))
  requests.append(req)

head = int(input("Intial head position: "))

disk_max = int(input("Enter the maximum track number: "))

direction = input("Enter initial head direction (left/right): ").strip().lower()
if direction not in ("left", "right"):
    print("Invalid direction, assuming 'right'.")
    direction = "right"

requests.sort()

current_position = head
total_movement = 0

print("\nRequests\tHead Movement")

