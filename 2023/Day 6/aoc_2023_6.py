import re
import numpy as np

record_times_file = open("2023/Day 6/input.txt", "r")
record_times = record_times_file.read()
record_times_file.close()

record_times_lines = record_times.splitlines()

# pt 1 -----------------------------------------------------------------------------
times = np.array([int(n) for n in re.findall("\d+", record_times_lines[0])])
distances = np.array([int(n) for n in re.findall("\d+", record_times_lines[1])])

def distance_traveled(total_time, held_down_time):
    dist = held_down_time*(total_time - held_down_time)
    return dist

ways_to_beat = list()

race_0_distances = np.array([distance_traveled(times[0], t) for t in range(times[0])])
race_1_distances = np.array([distance_traveled(times[1], t) for t in range(times[1])])
race_2_distances = np.array([distance_traveled(times[2], t) for t in range(times[2])])
race_3_distances = np.array([distance_traveled(times[3], t) for t in range(times[3])])

ways_to_beat.append(sum(race_0_distances > distances[0]))
ways_to_beat.append(sum(race_1_distances > distances[1]))
ways_to_beat.append(sum(race_2_distances > distances[2]))
ways_to_beat.append(sum(race_3_distances > distances[3]))

answer_pt_1 = np.prod(ways_to_beat)

# pt 2 -----------------------------------------------------------------------------

# If D is the record distance, T is the total race time, and t in [0,T] is the held down time,
# then we just need to find the roots of d(t) - D = t(T-t) - D = 0.

def find_roots(a, b, c):
    x1 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)

    return [x1, x2]


T = int(re.sub("\D", "",  record_times_lines[0]))
D = int(re.sub("\D", "",  record_times_lines[1]))

roots = find_roots(-1, T, -D)

ways_2_beat = np.floor(roots[0]) - np.floor(roots[1])