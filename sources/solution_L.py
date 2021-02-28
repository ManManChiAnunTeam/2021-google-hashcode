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
        for p in path:
            if p not in street_count:
                street_count[p] = 1
            else:
                street_count[p] += 1

    # solution
    answer = [[] for _ in range(inter_n)]
    for i in range(car_n):
        for p in cars[i]:
            if p not in street_count:
                street_count[p] = 1
            else:
                street_count[p] += 1
    values = set()
    for i in range(inter_n):
        for e, name, L in adj[i]:
            if name not in street_count:
                continue
            answer[e].append((name, 1/L))
            values.add(1/L)
    MAX_L = max(values)

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
        for name, L in answer[i]:
            MAX_TIME = 30 # simulated annealing
            print(name, max(1, int(MAX_TIME * L / MAX_L)))

if __name__ == "__main__":
    f_names = ['a', 'b', 'c', 'd', 'e', 'f']
    for f_name in f_names:
        sys.stdin = open(f_name + '.txt', 'r')
        sys.stdout = open(f_name + "_output_L.txt", 'w')
        solution()