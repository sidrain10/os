n = int(input("Enter the number of disk requests: "))

requests = []
for i in range(n): 
  req = int(input(f"Enter the request {i+1}: "))
  requests.append(req)

head = int(input("Intial head position: "))


done = [False] * n  
current_position = head
total_movement = 0
completed = 0

print("\nRequest\tHead Movement")

while completed < n:
  pending = [i for i in range(n) if not done[i]]

  closest = min(pending, key = lambda i : abs(requests[i] - current_position))

  movement = abs(requests[closest] - current_position)
  total_movement += movement

  print(f"{requests[closest]}\t{movement}")
  
  current_position = requests[closest]
  done[closest] = True
  completed += 1

print("\nFinal Head Position =", current_position)
print("Total Head Movement =", total_movement)  

  