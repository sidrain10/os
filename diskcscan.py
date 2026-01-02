n = int(input("disk requests: "))

requests = []

for i in range(n):
  req = int(input(f"Enter request {i+1}: "))
  requests.append(req)

head = int(input("Enter the initial head position: "))

disk_max = int(input("Enter max track number: "))

direction = input("Enter direction (left/right): ").strip().lower()
if direction not in ("right", "left"):
  print("invalid direction, assuming right!")
  direction = "right"

requests.sort()

current_position = head
total_movement = 0


print("\nRequest\tMovement")

if direction == "right":
  right = [r for r in requests if r >= head]

  left = [r for r in requests if r < head]


  for req in right: 
    movement = abs(req - current_position)
    total_movement += movement
    print(f"{req}\t{movement}")
    current_position = req

  if current_position != disk_max:
    movement = abs(disk_max - current_position)
    total_movement += movement
    print(f"end({disk_max})\t{movement}")
    current_position = disk_max  

  movement = abs(current_position - 0)
  total_movement += movement
  print(f"Jump(0)\t{movement}")
  current_position = 0


  for req in left: 
    movement = abs(req - current_position)
    total_movement += movement
    print(f"{req}\t{movement}")  
    current_position = req


else:

  left = [r for r in requests if r <=head][::-1]
  right = [r for r in requests if r > head][::-1]

  
