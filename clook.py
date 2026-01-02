n = int(input("Enter the number of disk requests: "))

requests = []
for i in range(n):
    req = int(input(f"Enter request {i+1}: "))
    requests.append(req)

head = int(input("Enter initial head position: "))

direction = input("Enter initial head direction (left/right): ").strip().lower()
if direction not in ("left", "right"):
    print("Invalid direction, assuming 'right'.")
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

    if left:
        jump_target = left[0]
        jump_movement = abs(current_position - jump_target)
        total_movement += jump_movement
        print(f"Jump({jump_target})\t{jump_movement}")
        current_position = jump_target

        for req in left:
            movement = abs(req - current_position)
            total_movement += movement
            print(f"{req}\t{movement}")
            current_position = req

else: 
    left = [r for r in requests if r <= head][::-1]
    right = [r for r in requests if r > head][::-1]

    for req in left:
        movement = abs(req - current_position)
        total_movement += movement
        print(f"{req}\t{movement}")
        current_position = req

    if right:
        jump_target = right[0]  
        jump_movement = abs(current_position - jump_target)
        total_movement += jump_movement
        print(f"Jump({jump_target})\t{jump_movement}")
        current_position = jump_target

        for req in right:
            movement = abs(req - current_position)
            total_movement += movement
            print(f"{req}\t{movement}")
            current_position = req

print("\nFinal Head Position =", current_position)
print("Total Head Movement =", total_movement)
