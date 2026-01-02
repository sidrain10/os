n = int(input("Enter the number of disk requests: "))

requests = []
for i in range(n): 
  req = int(input(f"Enter the request {i+1}: "))
  requests.append(req)

head = int(input("Intial head position: "))

total_movement = 0
current_position = head

print("\nRequest\tHead Movement")

for req in requests:
  movement = abs(req - current_position)
  total_movement += movement

  print(f"{req}\t{movement}")

  current_position = req

print(f"Final head position: {current_position}")
print(f"Total Head Movement: {total_movement}")
