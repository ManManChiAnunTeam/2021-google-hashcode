import sys

def solution():
    # input
    # points : (duration - T) + bonus
    duration, inter_n, street_n, car_n, bonus = map(int, input().split())
    adj = [list() for _ in range(inter_n)]
    name_to_street = {}
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
    answer = [[] for _ in range(inter_n)]
    for i in range(inter_n):
        for e, name, L in adj[i]:
            answer[e].append((name, 1))

    # output
    # A : the number of intersections for which you specify the schedule
    A = 0
    for i in range(inter_n):
        if answer[i]:
            A += 1
    for i in range(A):
        # i : id
        # E : number of incoming
        # E lines : street name , duration
        print(i)
        print(len(answer[i]))
        for name, d in answer[i]:
            print(name, d)

if __name__ == "__main__":
    f_names = ['a', 'b', 'c', 'd', 'e', 'f']
    for f_name in f_names:
        sys.stdin = open(f_name + '.txt', 'r')
        sys.stdout = open(f_name + "_output_1sec.txt", 'w')
        solution()