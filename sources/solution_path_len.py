import sys

def solution():
    # input
    # points : (duration - T) + bonus
    duration, inter_n, street_n, car_n, bonus = map(int, input().split())
    adj = [list() for _ in range(inter_n)]
    name_to_street = {}
    street_count = {}
    cars = []
    for _ in range(street_n):
        s, e, name, L = input().split()
        s, e, L = int(s), int(e), int(L)
        adj[s].append((e, name, L))
        name_to_street[name] = (s, e, L)
    for _ in range(car_n):
        path = input().split()
        cars.append(path[1:])

    # solution
    values = []
    for i in range(car_n):
        values.append(len(cars[i]))
    mid1_CC = sorted(values)[len(values)//3]
    mid2_CC = sorted(values)[2*len(values)//3]
    for i in range(car_n):
        t = 1
        if values[i] < mid2_CC: t = 2
        if values[i] < mid1_CC: t = 3
        for p in cars[i]:
            if p not in street_count:
                street_count[p] = t
            else:
                street_count[p] += t
    MAX_CC = max(street_count.values())
    answer = [[] for _ in range(inter_n)]
    for i in range(inter_n):
        for e, name, L in adj[i]:
            if name not in street_count:
                continue
            answer[e].append((name, street_count[name]))

    # output
    # A : the number of intersections for which you specify the schedule
    A = 0
    for i in range(inter_n):
        if answer[i]:
            A += 1
    print(A)
    for i in range(inter_n):
        if not answer[i]:
            continue
        # i : id
        # E : number of incoming
        # E lines : street name , duration
        print(i)
        print(len(answer[i]))
        for name, CC in answer[i]:
            MAX_TIME = 30 # simulated annealing
            print(name, max(1, int(MAX_TIME * CC / MAX_CC)))

if __name__ == "__main__":
    f_names = ['a', 'b', 'c', 'd', 'e', 'f']
    for f_name in f_names:
        sys.stdin = open(f_name + '.txt', 'r')
        sys.stdout = open(f_name + "_output_path_len.txt", 'w')
        solution()