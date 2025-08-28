distance = int(input())
tank_range = int(input())
stops = int(input())
stop_distance = list(map(int, input().split()))
stop_distance = [0] + stop_distance + [distance]

refill = 0
current_pos = 0
n = len(stop_distance)

while current_pos < n - 1:
    last_pos = current_pos

    # Move as far forward as we can within tank range
    while (current_pos < n - 1 and
           stop_distance[current_pos + 1] - stop_distance[last_pos] <= tank_range):
        current_pos += 1

    if current_pos == last_pos:
        # Can't move forward — no reachable station
        refill = -1
        break

    if current_pos < n - 1:
        # Need to refill here
        refill += 1

print(refill)
